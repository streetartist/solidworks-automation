# ITabAndSlotFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData`

Allows access to a tab and slot feature.
Allows access to a tab and slot feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ITabAndSlotFeatureData 
```

```

Dim instance As ITabAndSlotFeatureData
```

```

public interface ITabAndSlotFeatureData 
```

```

public interface class ITabAndSlotFeatureData 
```

Example

'VBA

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
' 1. Open *public\_documents***\samples\whatsnew\sheet metal\tab\_and\_slot.sldprt**.  
' 2. Run this macro until the Stop.  
' 3. Select **Tab and Slot-Tab1** in the FeatureManager design tree;  
'     5 tabs/slots created  
' 4. Press F5 to continue.  
' 5. Select **Tab and Slot-Tab1** in the FeatureManager design tree;  
'     1 tab/slot remains  
  
' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Dim swApp As SldWorks.SldWorks  
Dim featdata As TabAndSlotFeatureData  
Dim grp As SldWorks.TabAndSlotGroupData  
Dim Part As SldWorks.ModelDoc2  
Dim swedge As SldWorks.Edge  
Dim swface As SldWorks.Face2  
Dim feat As SldWorks.Feature  
Dim newFeatData As SldWorks.TabAndSlotFeatureData  
Dim boolstatus As Boolean

Option Explicit  
Sub main()

> Set swApp = Application.SldWorks  
> Set Part = swApp.ActiveDoc  
>   
> boolstatus = Part.Extension.SelectByRay(-5.81596588411344E-02, 2.47654446213232E-02, 2.34517259855238E-04, -0.577381545199981, -0.577287712085548, -0.577381545199979, 1.57359077741066E-03, 1, False, 0, 0)  
> Set swedge = Part.SelectionManager.GetSelectedObject6(1, -1)  
> Part.ClearSelection2 True  
>   
> boolstatus = Part.Extension.SelectByRay(-1.33680887414585E-02, -9.08584763345743E-03, -1.99999999999534E-03, -0.821234743714012, -0.560561193384781, 0.106511239726198, 1.57359077741066E-03, 2, False, 0, 0)  
> Set swface = Part.SelectionManager.GetSelectedObject6(1, -1)  
> Part.ClearSelection2 True  
>   
> Set featdata = Part.FeatureManager.**CreateDefinition**(swFmTabAndSlot)  
>   
> Set grp = featdata.**SelectionAddNewGroup**  
> grp.**Offset** = True  
> grp.**SelectionTabEdge** = swedge  
> grp.**SelectionSlotFace** = swface  
> Part.FeatureManager.**CreateFeature** featdata  
>   
> Stop  
> ' Select **Tab and Slot-Tab1** in the FeatureManager design tree; 5 tabs/slots created on the part  
> ' Press F5 to continue  
>   
> Set feat = Part.SelectionManager.GetSelectedObject6(1, -1)  
> Set newFeatData = feat.**GetDefinition**  
> Dim var As Variant  
> newFeatData.**AccessSelections** Part, Nothing  
> var = newFeatData.**SelectionGetGroups**  
> var(0).**Offset** = False  
> var(0).**SpacingType** = 0  
> var(0).**SpacingNumberOfInstances** = 1  
> feat.**ModifyDefinition** newFeatData, Part, Nothing  
>   
> ' Select **Tab and Slot-Tab1** in the FeatureManager design tree; only one tab and slot remain

End Sub

Example

[Create Tab and Slot (C#)](Create_Tab_And_Slot_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)
