# ISetBodies Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetBodies`

Sets the bodies of a multibody part to include in the view.
Sets the bodies of a multibody part to include in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetBodies( _
   ByVal Count As System.Integer, _
   ByRef BodyArray As Body2 _
) 
```

```

Dim instance As IView
Dim Count As System.Integer
Dim BodyArray As Body2
 
instance.ISetBodies(Count, BodyArray)
```

```

void ISetBodies( 
   System.int Count,
   ref Body2 BodyArray
)
```

```

void ISetBodies( 
   System.int Count,
   Body2^% BodyArray
) 
```

#### Parameters

*Count*
:   Number of bodies in a multibody part

*BodyArray*
:   - in-process, unmanaged C++: Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBodies.md)  
[IView::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Bodies.md)
