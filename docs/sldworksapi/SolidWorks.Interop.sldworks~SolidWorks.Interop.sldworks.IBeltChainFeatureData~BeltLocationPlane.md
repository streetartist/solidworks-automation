# BeltLocationPlane Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltLocationPlane`

Gets and sets the belt location plane.
Gets and sets the belt location plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BeltLocationPlane As System.Object
```

```

Dim instance As IBeltChainFeatureData
Dim value As System.Object
 
instance.BeltLocationPlane = value
 
value = instance.BeltLocationPlane
```

```

System.object BeltLocationPlane {get; set;}
```

```

property System.Object^ BeltLocationPlane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

The belt sketch plane is normal to the pulley axes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)
