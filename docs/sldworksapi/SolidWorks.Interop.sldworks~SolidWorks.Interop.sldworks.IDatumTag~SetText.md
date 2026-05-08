# SetText Method (IDatumTag)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetText`

Sets the text of this datum tag.
Sets the text of this datum tag.

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

Dim instance As IDatumTag
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
:   Text to set as defined in [swDatumTagTextParts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumTagTextParts_e.html)

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

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)
