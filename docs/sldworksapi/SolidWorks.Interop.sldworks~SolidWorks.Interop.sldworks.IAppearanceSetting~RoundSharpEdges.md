# RoundSharpEdges Property (IAppearanceSetting)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~RoundSharpEdges`

Gets or sets the value by which to round sharp edges when rendering a model using a ray-trace rendering engine.
Gets or sets the value by which to round sharp edges when rendering a model using a ray-trace rendering engine.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RoundSharpEdges As System.Double
```

```

Dim instance As IAppearanceSetting
Dim value As System.Double
 
instance.RoundSharpEdges = value
 
value = instance.RoundSharpEdges
```

```

System.double RoundSharpEdges {get; set;}
```

```

property System.double RoundSharpEdges {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Value by which to round sharp edges

Remarks

This method:

- is only available when a ray-trace rendering engine is loaded.
- does not change model geometry.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md)  
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.md)
