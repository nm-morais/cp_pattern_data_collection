#ifndef __PATTERNS_H_SEQ
#define __PATTERNS_H_SEQ


void mapSeq (
  void *dest,           // Target array
  void *src,            // Source array
  size_t nJob,          // # elements in the source array
  size_t sizeJob,       // Size of each element in the source array
  void (*worker)(void *v1, const void *v2) // [ v1 = op (v2) ]
);

void reduceSeq (
  void *dest,           // Target array
  void *src,            // Source array
  size_t nJob,          // # elements in the source array
  size_t sizeJob,       // Size of each element in the source array
  void (*worker)(void *v1, const void *v2, const void *v3) // [ v1 = op (v2, v3) ]
);

void scanSeq (
  void *dest,           // Target array
  void *src,            // Source array
  size_t nJob,          // # elements in the source array
  size_t sizeJob,       // Size of each element in the source array
  void (*worker)(void *v1, const void *v2, const void *v3) // [ v1 = op (v2, v3) ]
);

int packSeq (
  void *dest,           // Target array
  void *src,            // Source array
  size_t nJob,          // # elements in the source array
  size_t sizeJob,       // Size of each element in the source array
  const int *filter     // Filer for pack
);

void gatherSeq (
  void *dest,           // Target array
  void *src,            // Source array
  size_t nJob,          // # elements in the source array
  size_t sizeJob,       // Size of each element in the source array
  const int *filter,    // Filter for gather
  int nFilter           // # elements in the filter
);

void scatterSeq (
  void *dest,           // Target array
  void *src,            // Source array
  size_t nJob,          // # elements in the source array
  size_t sizeJob,       // Size of each element in the source array
  const int *filter     // Filter for scatter
);

void pipelineSeq (
  void *dest,           // Target array
  void *src,            // Source array
  size_t nJob,          // # elements in the source array
  size_t sizeJob,       // Size of each element in the source array
  void (*workerList[])(void *v1, const void *v2), // one function for each stage of the pipeline
  size_t nWorkers       // # stages in the pipeline
);

void farmSeq (
  void *dest,           // Target array
  void *src,            // Source array
  size_t nJob,          // # elements in the source array
  size_t sizeJob,       // Size of each element in the source array
  void (*worker)(void *v1, const void *v2),  // [ v1 = op (22) ]
  size_t nWorkers       // # workers in the farm
);

#endif