# YLabel Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~YLabel`

Gets or sets the label for the Y axis for this datum origin.
Gets or sets the label for the Y axis for this datum origin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property YLabel As System.String
```

```

Dim instance As IDatumOrigin
Dim value As System.String
 
instance.YLabel = value
 
value = instance.YLabel
```

```

System.string YLabel {get; set;}
```

```

property System.String^ YLabel {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Label for the Y axis for this datum origin

Example

[Get Labels of Datum Origin (C#)](Get_Labels_of_Datum_Origin_Example_CSharp.htm)  
[Get Labels of Datum Origin (VB.NET)](Get_Labels_of_Datum_Origin_Example_VBNET.htm)  
[Get Labels of Datum Origin (VBA)](Get_Labels_of_Datum_Origin_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md)  
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.md)  
[IDatumOrigin::XLabel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~XLabel.md)
