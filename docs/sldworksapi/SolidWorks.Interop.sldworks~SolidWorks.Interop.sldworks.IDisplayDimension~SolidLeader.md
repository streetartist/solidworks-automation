# SolidLeader Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SolidLeader`

Gets or sets whether this display dimension is displayed with a solid leader for arc and radial dimensions.
Gets or sets whether this display dimension is displayed with a solid leader for arc and radial dimensions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SolidLeader As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.SolidLeader = value
 
value = instance.SolidLeader
```

```

System.bool SolidLeader {get; set;}
```

```

property System.bool SolidLeader {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True displays a solid leader, false does not

Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetBrokenLeader2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBrokenLeader2.md)  
[IDisplayDimension::GetUseDocBrokenLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBrokenLeader.md)  
[IDisplayDimension::GetBrokenLeader2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBrokenLeader2.md)
