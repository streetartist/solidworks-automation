# GetGtolFormatData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFormatData`

Gets the Gtol format and XML schema versions supported by this version of SOLIDWORKS.
Gets the Gtol format and XML schema versions supported by this version of SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetGtolFormatData( _
   ByRef GtolFormat As System.Integer, _
   ByRef XmlSchemaversion As System.Integer _
) 
```

```

Dim instance As ISldWorks
Dim GtolFormat As System.Integer
Dim XmlSchemaversion As System.Integer
 
instance.GetGtolFormatData(GtolFormat, XmlSchemaversion)
```

```

void GetGtolFormatData( 
   out System.int GtolFormat,
   out System.int XmlSchemaversion
)
```

```

void GetGtolFormatData( 
   [Out] System.int GtolFormat,
   [Out] System.int XmlSchemaversion
) 
```

#### Parameters

*GtolFormat*
:   Gtol format as defined by [swGtolFormatType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolFormatType_e.html)

*XmlSchemaversion*
:   XML schema version as defined by [swGtolFormatSchemaVersion\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolFormatSchemaVersion_e.html)

Remarks

See [Gtol Frame XML Schema](ms-its:sldworksapiprogguide.chm::/Overview/Gtol_Frame_XML_Schema.htm).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetGtolFrameXMLSchema Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFrameXMLSchema.md)
