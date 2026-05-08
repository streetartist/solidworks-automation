# InsertBOMBalloon2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertBOMBalloon2`

Obsolete. Superseded by IModelDoc2::InsertBOMBalloon2.
Obsolete. Superseded by [IModelDoc2::InsertBOMBalloon2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBOMBalloon2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBOMBalloon2( _
   ByVal Style As System.Integer, _
   ByVal Size As System.Integer, _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String _
) As System.Object
```

```

Dim instance As IModelDoc
Dim Style As System.Integer
Dim Size As System.Integer
Dim UpperTextStyle As System.Integer
Dim UpperText As System.String
Dim LowerTextStyle As System.Integer
Dim LowerText As System.String
Dim value As System.Object
 
value = instance.InsertBOMBalloon2(Style, Size, UpperTextStyle, UpperText, LowerTextStyle, LowerText)
```

```

System.object InsertBOMBalloon2( 
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.string UpperText,
   System.int LowerTextStyle,
   System.string LowerText
)
```

```

System.Object^ InsertBOMBalloon2( 
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.String^ UpperText,
   System.int LowerTextStyle,
   System.String^ LowerText
) 
```

#### Parameters

*Style*

*Size*

*UpperTextStyle*

*UpperText*

*LowerTextStyle*

*LowerText*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
