# ReverseDirection Property (IGroundPlaneFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData~ReverseDirection`

Gets or sets whether to reverse direction of alignment in this ground plane feature.
Gets or sets whether to reverse direction of alignment in this ground plane feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseDirection As System.Boolean
```

```

Dim instance As IGroundPlaneFeatureData
Dim value As System.Boolean
 
instance.ReverseDirection = value
 
value = instance.ReverseDirection
```

```

System.bool ReverseDirection {get; set;}
```

```

property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the alignment of assembly faces relative to the ground plane, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGroundPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.md)  
[IGroundPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData_members.md)
