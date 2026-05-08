# SetText Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetText`

Sets the specified text part of this GTol.
Sets the specified text part of this GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetText( _
   ByVal WhichText As System.Integer, _
   ByVal Text As System.String _
) As System.Boolean
```

```

Dim instance As IGtol
Dim WhichText As System.Integer
Dim Text As System.String
Dim value As System.Boolean
 
value = instance.SetText(WhichText, Text)
```

```

System.bool SetText( 
   System.int WhichText,
   System.string Text
)
```

```

System.bool SetText( 
   System.int WhichText,
   System.String^ Text
) 
```

#### Parameters

*WhichText*
:   Text to set as defined in [swGTolTextParts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGTolTextParts_e.html)

*Text*
:   New content for the specified WhichText

#### Return Value

True if successful, false if not

Remarks

After calling this method, call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) to see the new text.

Example

[Set Text in Datum Tags and GTols (VBA)](Set_Text_in_Datum_Tags_and_GTols_Example_VB.htm)  
[Set Text in Datum Tags and GTols (VB.NET)](Set_Text_in_Datum_Tags_and_GTols_Example_VBNET.htm)  
[Set Text in Datum Tags and GTols (C#)](Set_Text_in_Datum_Tags_and_GTols_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetText.md)
