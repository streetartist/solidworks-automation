# DimensionDisplay Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~DimensionDisplay`

Gets whether dimensions are displayed.
Gets whether dimensions are displayed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DimensionDisplay As System.Boolean
```

```

Dim instance As ISketchBlockInstance
Dim value As System.Boolean
 
instance.DimensionDisplay = value
 
value = instance.DimensionDisplay
```

```

System.bool DimensionDisplay {get; set;}
```

```

property System.bool DimensionDisplay {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if dimensions are displayed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)  
[ISketchBlockDefinition::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensions.md)  
[ISketchBlockDefinition::IGetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetDisplayDimensions.md)  
[ISketchBlockDefinition::GetDisplayDimensionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensionCount.md)
