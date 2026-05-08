# GetGtolFrameXMLSchema Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFrameXMLSchema`

Gets the XML schema for Gtol frame symbol XML.
Gets the XML schema for Gtol frame symbol XML.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGtolFrameXMLSchema() As System.String
```

```

Dim instance As ISldWorks
Dim value As System.String
 
value = instance.GetGtolFrameXMLSchema()
```

```

System.string GetGtolFrameXMLSchema()
```

```

System.String^ GetGtolFrameXMLSchema(); 
```

#### Return Value

XML schema for Gtol Frame symbol XML

Remarks

See [Gtol Frame XML Schema](ms-its:sldworksapiprogguide.chm::/Overview/Gtol_Frame_XML_Schema.htm).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[IGtolFrame::GetSymbolXml Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetSymbolXml.md)  
[IGtolFrame::SetSymbolXml Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~SetSymbolXml.md)  
[ISldWorks::GetGtolFormatData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFormatData.md)
