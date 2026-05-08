# ClearSelection2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2`

Clears the selection list.
Clears the selection list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ClearSelection2( _
   ByVal All As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim All As System.Boolean
 
instance.ClearSelection2(All)
```

```

void ClearSelection2( 
   System.bool All
)
```

```

void ClearSelection2( 
   System.bool All
) 
```

#### Parameters

*All*
:   True clears the entire existing selection list, false clears only the items in the active selection list (see **Remarks**)

Remarks

False only works if the current PropertyManager page contains a selection list; otherwise, this method clears all selections.

Example

[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)  
[Get Bodies (C++)](Get_Bodies_Example_CPlusPlus_COM.htm)  
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)  
[Add Distance Mates (VBA)](Add_Distance_Mates_Example_VB.htm)  
[Create Plane Thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)  
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)  
[Insert a Note (VBA)](Insert_a_Note_Example_VB.htm)  
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)  
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)  
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISelectionMgr::SuspendSelectionList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SuspendSelectionList.md)
