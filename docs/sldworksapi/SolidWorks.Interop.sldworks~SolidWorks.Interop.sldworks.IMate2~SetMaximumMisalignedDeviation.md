# SetMaximumMisalignedDeviation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetMaximumMisalignedDeviation`

Sets the maximum allowed misalignment deviation for this misaligned concentric mate.
Sets the maximum allowed misalignment deviation for this misaligned concentric mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetMaximumMisalignedDeviation( _
   ByVal MaximumDeviation As System.Double _
) 
```

```

Dim instance As IMate2
Dim MaximumDeviation As System.Double
 
instance.SetMaximumMisalignedDeviation(MaximumDeviation)
```

```

void SetMaximumMisalignedDeviation( 
   System.double MaximumDeviation
)
```

```

void SetMaximumMisalignedDeviation( 
   System.double MaximumDeviation
) 
```

#### Parameters

*MaximumDeviation*
:   Maximum allowed misalignment deviation

Remarks

This method is valid only if [IMate2::GetUseMisalignedDeviationDocumentProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetUseMisalignedDeviationDocumentProperty.md) returns false. Call [IMate2::SetUseMisalignedDeviationDocumentProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetUseMisalignedDeviationDocumentProperty.md) to set UseDocumentProperty to false if you want to use this method to set the maximum misaligned deviation for this mate.

If [IMate2::GetCurrentMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetCurrentMisalignedDeviation.md) is greater than the value set by this method, then the mate fails to solve.

The current deviation and the maximum deviation are cumulative across both concentric mates in the Hole Set. For example, if [IMate2::GetConcentricAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.md) is set to [swConcentricAlignmentType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html).swConcentricAlignSymmetric, the deviation from both holes is summed before comparison with the maximum deviation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::GetMaximumMisalignedDeviation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMaximumMisalignedDeviation.md)
