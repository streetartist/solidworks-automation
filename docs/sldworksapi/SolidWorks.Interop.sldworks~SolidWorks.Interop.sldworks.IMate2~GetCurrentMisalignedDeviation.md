# GetCurrentMisalignedDeviation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetCurrentMisalignedDeviation`

Gets the current misalignment deviation for the misaligned concentric mate.
Gets the current misalignment deviation for the misaligned concentric mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurrentMisalignedDeviation() As System.Double
```

```

Dim instance As IMate2
Dim value As System.Double
 
value = instance.GetCurrentMisalignedDeviation()
```

```

System.double GetCurrentMisalignedDeviation()
```

```

System.double GetCurrentMisalignedDeviation(); 
```

#### Return Value

Current misalignment deviation

Remarks

If the current deviation of misalignment is greater than [IMate2::GetMaximumMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMaximumMisalignedDeviation.md), then the mate fails to solve.

The current deviation and the maximum deviation are cumulative across both concentric mates in the Hole Set. For example, if [IMate2::GetConcentricAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.md) is set to [swConcentricAlignmentType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html).swConcentricAlignSymmetric, the deviation from both holes is summed before comparison with the maximum deviation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)
