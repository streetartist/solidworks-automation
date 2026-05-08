# GetSymbolXml Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetSymbolXml`

Gets the XML string for this Gtol frame.
Gets the XML string for this Gtol frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSymbolXml() As System.String
```

```

Dim instance As IGtolFrame
Dim value As System.String
 
value = instance.GetSymbolXml()
```

```

System.string GetSymbolXml()
```

```

System.String^ GetSymbolXml(); 
```

#### Return Value

XML string for this Gtol frame

Remarks

This method is valid only for Gtols created in or converted to the SOLIDWORKS 2022 format.

See [Gtol Frame XML Schema](ms-its:sldworksapiprogguide.chm::/Overview/Gtol_Frame_XML_Schema.htm).

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtolFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md)  
[IGtolFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame_members.md)  
[ISldWorks::GetGtolFrameXMLSchema Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFrameXMLSchema.md)  
[IGtolFrame::SetSymbolXml Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~SetSymbolXml.md)
