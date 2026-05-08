# ScaleHatchPattern Property (IDrSection)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ScaleHatchPattern`

Gets or sets whether to scale the hatch pattern to the section view.
Gets or sets whether to scale the hatch pattern to the section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleHatchPattern As System.Boolean
```

```

Dim instance As IDrSection
Dim value As System.Boolean
 
instance.ScaleHatchPattern = value
 
value = instance.ScaleHatchPattern
```

```

System.bool ScaleHatchPattern {get; set;}
```

```

property System.bool ScaleHatchPattern {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to scale the hatch pattern to the section view, false to not

Example

[Scale Hatch Pattern to Section View (C#)](Scale_Hatch_Pattern_With_Section_View_Example_CSharp.htm)  
[Scale Hatch Pattern to Section View (VB.NET)](Scale_Hatch_Pattern_With_Section_View_Example_VBNET.htm)  
[Scale Hatch Pattern to Section View (VBA)](Scale_Hatch_Pattern_With_Section_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::GetAutoHatch Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetAutoHatch.md)  
[IDrSection::SetAutoHatch Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetAutoHatch.md)  
[IDrSection::RandomizeScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~RandomizeScale.md)
