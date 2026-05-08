# ReplaceViewModel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReplaceViewModel`

Replaces the specified instances of a model in the specified drawing views.
Replaces the specified instances of a model in the specified drawing views.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReplaceViewModel( _
   ByVal NewModelPathName As System.String, _
   ByVal Views As System.Object, _
   ByVal Instances As System.Object _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim NewModelPathName As System.String
Dim Views As System.Object
Dim Instances As System.Object
Dim value As System.Boolean
 
value = instance.ReplaceViewModel(NewModelPathName, Views, Instances)
```

```

System.bool ReplaceViewModel( 
   System.string NewModelPathName,
   System.object Views,
   System.object Instances
)
```

```

System.bool ReplaceViewModel( 
   System.String^ NewModelPathName,
   System.Object^ Views,
   System.Object^ Instances
) 
```

#### Parameters

*NewModelPathName*
:   Full path and filename of the replacement model

*Views*
:   Array of [IView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)s in which to replace the model

*Instances*
:   Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s that are specific instances of the model to replace in the drawing

#### Return Value

True if the model is replaced, false if not

Remarks

This method corresponds to **Tools > Replace Model**.

Example

[Replace View Model (C#)](Replace_View_Model_Example_CSharp.htm)  
[Replace View Model (VB.NET)](Replace_View_Model_Example_VBNET.htm)  
[Replace View Model (VBA)](Replace_View_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::InsertModelInPredefinedView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelInPredefinedView.md)
