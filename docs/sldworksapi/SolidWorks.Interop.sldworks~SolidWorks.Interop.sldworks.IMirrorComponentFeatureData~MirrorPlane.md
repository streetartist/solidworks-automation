# MirrorPlane Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorPlane`

Gets or sets the plane about which components are mirrored.
Gets or sets the plane about which components are mirrored.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MirrorPlane As System.Object
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Object
 
instance.MirrorPlane = value
 
value = instance.MirrorPlane
```

```

System.object MirrorPlane {get; set;}
```

```

property System.Object^ MirrorPlane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
