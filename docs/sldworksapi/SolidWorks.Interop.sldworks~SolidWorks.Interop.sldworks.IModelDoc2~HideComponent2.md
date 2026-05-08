# HideComponent2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~HideComponent2`

Hides the selected component.
Hides the selected component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub HideComponent2() 
```

```

Dim instance As IModelDoc2
 
instance.HideComponent2()
```

```

void HideComponent2()
```

```

void HideComponent2(); 
```

Remarks

This method is only available for [IDrawingDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md) and [IAssemblyDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md) objects; it is not available for [IPartDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md) objects.

To show a selected component, call [IModelDoc2::ShowComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowComponent2.md).

Example

[Undo Hidden Component and Fire Post-Notify Event (VB60](Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)  
[Undo Hidden Component and Fire Post-Notify Event (VB.NET)](Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)  
[Undo Hidden Component and Fire Post-Notify Event (C#)](Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ShowComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowComponent2.md)  
[IModelDoc2::IsActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsActive.md)
