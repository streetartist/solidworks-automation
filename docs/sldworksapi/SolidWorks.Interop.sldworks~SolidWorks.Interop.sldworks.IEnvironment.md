# IEnvironment Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment`

Allows you to analyze the text and geometry used to create a geometric tolerance symbol.
Allows you to analyze the text and geometry used to create a geometric tolerance symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IEnvironment 
```

```

Dim instance As IEnvironment
```

```

public interface IEnvironment 
```

```

public interface class IEnvironment 
```

Remarks

This interface can be useful if you have a note that contains a geometric tolerance symbol and you want to translate that note.

You can find the file containing the list of supported geometric tolerance symbols and their abbreviations in **C:\ProgramData\SolidWorks\SolidWorks 20***nn*\**lang**\**english\gtol.sym****.**  
**NOTE:** All numeric values returned from IEnvironment are relative to a unit text height of 1.0; i.e., if a geometric tolerance symbol has a text height of 0.15, then multiply the numeric values returned by 0.15.

Example

[Analyze Text and Geometry in GTol Symbol (C#)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_CSharp.htm)  
[Analyze Text and Geometry in GTol Symbol (VB.NET)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_VBNET.htm)  
[Analyze Text and Geometry in GTol Symbol (VBA)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
