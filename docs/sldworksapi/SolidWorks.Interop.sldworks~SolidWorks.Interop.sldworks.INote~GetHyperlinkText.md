# GetHyperlinkText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHyperlinkText`

Gets the hyperlink in a note.
Gets the hyperlink in a note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetHyperlinkText() As System.String
```

```

Dim instance As INote
Dim value As System.String
 
value = instance.GetHyperlinkText()
```

```

System.string GetHyperlinkText()
```

```

System.String^ GetHyperlinkText(); 
```

#### Return Value

Hyperlink text

Remarks

You can create an embedded hyperlink on a note by using [INote::SetHyperlinkText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHyperlinkText.md) or by using the hyperlink button on the note creation dialog.

This command first looks for an embedded hyperlink on the note and returns the text used to take the user to that document, which can be on the internet (a URL address is returned) or on your local network or hard drive (a pathname is returned). If the pathname was specified as a relative pathname, then the full pathname is returned.

If an embedded hyperlink does not exist, the note's text is searched for a hyperlink explicitly entered as part of the note text. This could be a URL address (a text string beginning with http://) or a file address (a text string beginning with file://).

If no hyperlink is found, either embedded or explicitly entered within the note text, an empty string is returned.

Example

[Remove Hyperlink From Note in Drawing (VBA)](Remove_Hyperlink_from_Note_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::SetHyperlinkText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHyperlinkText.md)
