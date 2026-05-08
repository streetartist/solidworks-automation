# SetUseMisalignedDeviationDocumentProperty Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetUseMisalignedDeviationDocumentProperty`

Sets whether to use the document property value for the maximum misalignment deviation for the misaligned concentric mate.
Sets whether to use the document property value for the maximum misalignment deviation for the misaligned concentric mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetUseMisalignedDeviationDocumentProperty( _
   ByVal UseDocumentProperty As System.Boolean _
) 
```

```

Dim instance As IMate2
Dim UseDocumentProperty As System.Boolean
 
instance.SetUseMisalignedDeviationDocumentProperty(UseDocumentProperty)
```

```

void SetUseMisalignedDeviationDocumentProperty( 
   System.bool UseDocumentProperty
)
```

```

void SetUseMisalignedDeviationDocumentProperty( 
   System.bool UseDocumentProperty
) 
```

#### Parameters

*UseDocumentProperty*
:   True to use the document property value for maximum misalignment deviation, false to not

Remarks

If [IMate2::GetCurrentMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetCurrentMisalignedDeviation.md) is greater than the document property value of the maximum misalignment deviation, then the mate fails to solve.

The current deviation and the maximum deviation are cumulative across both concentric mates in the Hole Set. For example, if [IMate2::GetConcentricAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.md) is set to [swConcentricAlignmentType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html).swConcentricAlignSymmetric, the deviation from both holes is summed before comparison with the maximum deviation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::GetUseMisalignedDeviationDocumentProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetUseMisalignedDeviationDocumentProperty.md)  
[IMate2::SetMaximumMisalignedDeviation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetMaximumMisalignedDeviation.md)
