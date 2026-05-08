# IGetDesignTableExtent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDesignTableExtent`

Gets the size and location of the design table associated with this drawing view.
Gets the size and location of the design table associated with this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDesignTableExtent() As System.Double
```

```

Dim instance As IView
Dim value As System.Double
 
value = instance.IGetDesignTableExtent()
```

```

System.double IGetDesignTableExtent()
```

```

System.double IGetDesignTableExtent(); 
```

#### Return Value

Array of 6 doubles; the lower left (x,y,z) and upper right (x,y,z) values indicating the design table extents; values are in meters and refer to drawing view space

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::HasDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~HasDesignTable.md)  
[IView::GetDesignTableExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDesignTableExtent.md)
