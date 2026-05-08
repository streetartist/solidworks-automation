# SetSymbolXml Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~SetSymbolXml`

Sets the XML string for this Gtol frame.
Sets the XML string for this Gtol frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSymbolXml( _
   ByVal Xmlstring As System.String _
) As System.Boolean
```

```

Dim instance As IGtolFrame
Dim Xmlstring As System.String
Dim value As System.Boolean
 
value = instance.SetSymbolXml(Xmlstring)
```

```

System.bool SetSymbolXml( 
   System.string Xmlstring
)
```

```

System.bool SetSymbolXml( 
   System.String^ Xmlstring
) 
```

#### Parameters

*Xmlstring*
:   XML string

#### Return Value

True if XML string successfully set, false if not

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
[IGtolFrame::GetSymbolXml Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetSymbolXml.md)
