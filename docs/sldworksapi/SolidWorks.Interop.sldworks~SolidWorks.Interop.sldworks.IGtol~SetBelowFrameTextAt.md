# SetBelowFrameTextAt Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBelowFrameTextAt`

Edits or inserts a text line at the specified below frame line index of this GTol.
Edits or inserts a text line at the specified below frame line index of this GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBelowFrameTextAt( _
   ByVal Index As System.Integer, _
   ByVal Text As System.String, _
   ByVal Overwrite As System.Boolean _
) As System.Boolean
```

```

Dim instance As IGtol
Dim Index As System.Integer
Dim Text As System.String
Dim Overwrite As System.Boolean
Dim value As System.Boolean
 
value = instance.SetBelowFrameTextAt(Index, Text, Overwrite)
```

```

System.bool SetBelowFrameTextAt( 
   System.int Index,
   System.string Text,
   System.bool Overwrite
)
```

```

System.bool SetBelowFrameTextAt( 
   System.int Index,
   System.String^ Text,
   System.bool Overwrite
) 
```

#### Parameters

*Index*
:   1-based line index at which to edit or insert text

*Text*
:   New text

*Overwrite*
:   True to overwrite the text at Index; false to insert a new line at Index

#### Return Value

True if the text is successfully edited or inserted, false if not

Example

See **Set Text in Datum Tags and GTols** examples in [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::DeleteBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~DeleteBelowFrameTextAt.md)  
[IGtol::GetBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextAt.md)  
[IGtol::GetBelowFrameTextLineCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextLineCount.md)  
[IGtol::InsertBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~InsertBelowFrameTextAt.md)
