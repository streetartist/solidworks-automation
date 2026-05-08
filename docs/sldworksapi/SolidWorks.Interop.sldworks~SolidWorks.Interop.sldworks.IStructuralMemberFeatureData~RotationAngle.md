# RotationAngle Property (IStructuralMemberFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~RotationAngle`

Gets or sets the angle by which the structural member turns relative to the adjacent structural member.
Gets or sets the angle by which the structural member turns relative to the adjacent structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotationAngle As System.Double
```

```

Dim instance As IStructuralMemberFeatureData
Dim value As System.Double
 
instance.RotationAngle = value
 
value = instance.RotationAngle
```

```

System.double RotationAngle {get; set;}
```

```

property System.double RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)
