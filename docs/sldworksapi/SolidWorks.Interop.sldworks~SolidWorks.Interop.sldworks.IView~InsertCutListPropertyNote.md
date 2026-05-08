# InsertCutListPropertyNote Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertCutListPropertyNote`

Inserts a note that contains all of the cut list item properties of a sheet metal part.
Inserts a note that contains all of the cut list item properties of a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertCutListPropertyNote( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) 
```

```

Dim instance As IView
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
 
instance.InsertCutListPropertyNote(X, Y, Z)
```

```

void InsertCutListPropertyNote( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

void InsertCutListPropertyNote( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   x coordinate of the note

*Y*
:   y coordinate of the note

*Z*
:   z coordinate of the note

Remarks

This method requires a flat pattern drawing view.

Example

[Insert Cut List Item Property Note (VBA)](Insert_Cut_List_Item_Property_Note_Example_VB.htm)  
[Insert Cut List Item Property Note (VB.NET)](Insert_Cut_List_Item_Property_Note_Example_VBNET.htm)  
[Insert Cut List Item Property Note (C#)](Insert_Cut_List_Item_Property_Note_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
