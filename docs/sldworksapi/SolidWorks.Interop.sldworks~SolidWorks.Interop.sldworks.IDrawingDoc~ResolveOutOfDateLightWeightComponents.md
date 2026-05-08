# ResolveOutOfDateLightWeightComponents Method (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ResolveOutOfDateLightWeightComponents`

Resolves out-of-date lightweight components in the selected drawing view or drawing sheet.
Resolves out-of-date lightweight components in the selected drawing view or drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ResolveOutOfDateLightWeightComponents() As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim value As System.Boolean
 
value = instance.ResolveOutOfDateLightWeightComponents()
```

```

System.bool ResolveOutOfDateLightWeightComponents()
```

```

System.bool ResolveOutOfDateLightWeightComponents(); 
```

#### Return Value

True if out-of-date lightweight components are resolved, false if not

Remarks

This method also resolves a selected out-of-date lightweight component and any out-of-date lightweight sub-components, in a drawing document.

You must select a drawing view, drawing sheet, or an out-of-date lightweight component before using this method.

|  |  |
| --- | --- |
| **If...** | **Then...** |
| Drawing view is selected | All out-of-date lightweight components in that drawing view are resolved |
| Drawing sheet is selected | All-out-of-date lightweight components in that drawing sheet are resolved |
| Out-of-date lightweight component is selected | It and any out-of-date lightweight sub-components are resolved |
| Your selection is invalid | This method returns false |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.md)  
[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IDrawingDoc::ChangeComponentLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ChangeComponentLayer.md)  
[IDrawingDoc::OnComponentProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~OnComponentProperties.md)
