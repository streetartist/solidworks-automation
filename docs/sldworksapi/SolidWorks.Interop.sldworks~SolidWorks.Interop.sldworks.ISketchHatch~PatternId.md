# PatternId Property (ISketchHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~PatternId`

Gets the pattern ID for this sketch hatch.
Gets the pattern ID for this sketch hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternId As System.Integer
```

```

Dim instance As ISketchHatch
Dim value As System.Integer
 
instance.PatternId = value
 
value = instance.PatternId
```

```

System.int PatternId {get; set;}
```

```

property System.int PatternId {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Pattern ID as defined in install\_dir\lang\language\SLDWRKS.PTN

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)  
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.md)  
[ISketchHatch::Pattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Pattern.md)
