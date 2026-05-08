# SecondaryMemberType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryStructuralMemberFeatureData~SecondaryMemberType`

Gets the type of this secondary structure system member.
Gets the type of this secondary structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property SecondaryMemberType As System.Integer
```

```

Dim instance As ISecondaryStructuralMemberFeatureData
Dim value As System.Integer
 
value = instance.SecondaryMemberType
```

```

System.int SecondaryMemberType {get;}
```

```

property System.int SecondaryMemberType {
   System.int get();
}
```

#### Property Value

Secondary structure system member type as defined by [swStructureSystemMemberCreationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSystemMemberCreationType_e.html)

Example

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryStructuralMemberFeatureData.md)  
[ISecondaryStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryStructuralMemberFeatureData_members.md)
