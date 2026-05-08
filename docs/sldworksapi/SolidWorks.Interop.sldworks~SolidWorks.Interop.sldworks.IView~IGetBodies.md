# IGetBodies Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBodies`

Gets the bodies of a multibody part in the drawing view.
Gets the bodies of a multibody part in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBodies( _
   ByVal Count As System.Integer _
) As Body2
```

```

Dim instance As IView
Dim Count As System.Integer
Dim value As Body2
 
value = instance.IGetBodies(Count)
```

```

Body2 IGetBodies( 
   System.int Count
)
```

```

Body2^ IGetBodies( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of bodies of a multibody part in the drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IView::GetBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBodiesCount.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetBodies.md)  
[IView::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Bodies.md)
