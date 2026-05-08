# SwapMembers Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~SwapMembers`

Assigns the trim tool functionality to the other member of this two member corner treatment feature.
Assigns the trim tool functionality to the other member of this two member corner treatment feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SwapMembers() 
```

```

Dim instance As ITwoMemberCornerTreatmentFeatureData
 
instance.SwapMembers()
```

```

void SwapMembers()
```

```

void SwapMembers(); 
```

Remarks

The first member appearing in the corner group members list in the user interface is assigned the trim tool function. Use this method to re-assign the trim tool function to the second member.

This method is valid only if [ITwoMemberCornerTreatmentFeatureData::CornerTreatmentTrimType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~CornerTreatmentTrimType.md) is set to [swCornerTreatmentTrimType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html).:

- swCornerTreatmentTrim\_BodyTrim

   - or -

- swCornerTreatmentTrim\_PlanarTrim

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITwoMemberCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData.md)  
[ITwoMemberCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData_members.md)
