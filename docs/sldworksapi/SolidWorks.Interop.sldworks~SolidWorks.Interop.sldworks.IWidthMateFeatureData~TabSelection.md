# TabSelection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~TabSelection`

Gets or sets the tab references for this width mate.
Gets or sets the tab references for this width mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TabSelection As System.Object
```

```

Dim instance As IWidthMateFeatureData
Dim value As System.Object
 
instance.TabSelection = value
 
value = instance.TabSelection
```

```

System.object TabSelection {get; set;}
```

```

property System.Object^ TabSelection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of tab entities (see **Remarks**)

Remarks

The tab entities can include:

- Two parallel planar [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)
- Two non-parallel planar faces
- One cylindrical face or [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.md)  
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.md)
