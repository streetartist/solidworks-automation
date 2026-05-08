# Pattern Property (ISketchHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Pattern`

Gets or sets the hatch pattern (also called type or name) of the sketch hatch (for example, "Stars" or "Honeycomb"), which is a string from the sldwks.ptn file.
Gets or sets the hatch pattern (also called type or name) of the sketch hatch (for example, "Stars" or "Honeycomb"), which is a string from the **sldwks.ptn** file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Pattern As System.String
```

```

Dim instance As ISketchHatch
Dim value As System.String
 
instance.Pattern = value
 
value = instance.Pattern
```

```

System.string Pattern {get; set;}
```

```

property System.String^ Pattern {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the hatch pattern

Example

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)  
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.md)  
[ISketchHatch::PatternId Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~PatternId.md)
