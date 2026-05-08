# InsertBelowFrameTextAt Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~InsertBelowFrameTextAt`

Inserts the specified text at the specified line index in the below frame of this GTol.
Inserts the specified text at the specified line index in the below frame of this GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBelowFrameTextAt( _
   ByVal Index As System.Integer, _
   ByVal Text As System.String _
) As System.Boolean
```

```

Dim instance As IGtol
Dim Index As System.Integer
Dim Text As System.String
Dim value As System.Boolean
 
value = instance.InsertBelowFrameTextAt(Index, Text)
```

```

System.bool InsertBelowFrameTextAt( 
   System.int Index,
   System.string Text
)
```

```

System.bool InsertBelowFrameTextAt( 
   System.int Index,
   System.String^ Text
) 
```

#### Parameters

*Index*
:   1-based index where to insert the line of Text in the below frame

*Text*
:   Text to insert

#### Return Value

True if text line successfully inserted, false if not

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
[IGtol::SetBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBelowFrameTextAt.md)
