# IgnorePolylineWidth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~IgnorePolylineWidth`

Gets or sets whether to convert width polylines to solid fill hatches when importing to the part sketch.
Gets or sets whether to convert width polylines to solid fill hatches when importing to the part sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IgnorePolylineWidth As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim value As System.Boolean
 
instance.IgnorePolylineWidth = value
 
value = instance.IgnorePolylineWidth
```

```

System.bool IgnorePolylineWidth {get; set;}
```

```

property System.bool IgnorePolylineWidth {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to convert width polylines to solid fill hatches, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)
