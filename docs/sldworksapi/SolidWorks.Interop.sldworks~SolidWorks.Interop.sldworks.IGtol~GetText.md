# GetText Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetText`

Gets the specified text part of this GTol.
Gets the specified text part of this GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetText( _
   ByVal WhichText As System.Integer _
) As System.String
```

```

Dim instance As IGtol
Dim WhichText As System.Integer
Dim value As System.String
 
value = instance.GetText(WhichText)
```

```

System.string GetText( 
   System.int WhichText
)
```

```

System.String^ GetText( 
   System.int WhichText
) 
```

#### Parameters

*WhichText*
:   Text part to get as defined in [swGTolTextParts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGTolTextParts_e.html)

#### Return Value

Text part

Example

See **Set Text in Datum Tags and GTols** examples in [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::SetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetText.md)
