# WidthSelection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~WidthSelection`

Gets or sets the width references for this width mate.
Gets or sets the width references for this width mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property WidthSelection As System.Object
```

```

Dim instance As IWidthMateFeatureData
Dim value As System.Object
 
instance.WidthSelection = value
 
value = instance.WidthSelection
```

```

System.object WidthSelection {get; set;}
```

```

property System.Object^ WidthSelection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of planar [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) (see **Remarks**)

Remarks

The planar faces can include:

- Two parallel planar faces
- Two non-parallel planar faces

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.md)  
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.md)
