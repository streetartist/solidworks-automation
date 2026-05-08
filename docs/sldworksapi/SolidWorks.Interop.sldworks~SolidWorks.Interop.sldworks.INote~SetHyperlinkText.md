# SetHyperlinkText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHyperlinkText`

Sets the hyperlink in a note.
Sets the hyperlink in a note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetHyperlinkText( _
   ByVal Text As System.String _
) As System.Boolean
```

```

Dim instance As INote
Dim Text As System.String
Dim value As System.Boolean
 
value = instance.SetHyperlinkText(Text)
```

```

System.bool SetHyperlinkText( 
   System.string Text
)
```

```

System.bool SetHyperlinkText( 
   System.String^ Text
) 
```

#### Parameters

*Text*
:   Text for hyperlink

#### Return Value

True if the hyperlink is successfully set, false if not

Remarks

You can retrieve the hyperlink text using [INote::GetHyperlinkText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHyperlinkText.md).

The input text can be a URL address or the name of a document on the local network or on your local system. You must specify the full address for a URL address, starting with the http://. You can specify a file name on your local network or system either as a full pathname or pathname relative to the current document, for example, D:\parts\drawing1.slddrw, or drawing1.slddrw.

To remove the hyperlink from a note, use this method and specify non-hyperlinked text.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetHyperlinkText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHyperlinkText.md)
