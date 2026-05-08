# CheckInterference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference`

Obsolete. Superseded by IModeler::CheckInterference3.
Obsolete. Superseded by [IModeler::CheckInterference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CheckInterference( _
   ByVal Body1 As System.Object, _
   ByVal Body2 As System.Object, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef Body1InterferedFaceArray As System.Object, _
   ByRef Body2InterferedFaceArray As System.Object, _
   ByRef IntersectedBodyArray As System.Object _
) As System.Boolean
```

```

Dim instance As IModeler
Dim Body1 As System.Object
Dim Body2 As System.Object
Dim CoincidentInterference As System.Boolean
Dim Body1InterferedFaceArray As System.Object
Dim Body2InterferedFaceArray As System.Object
Dim IntersectedBodyArray As System.Object
Dim value As System.Boolean
 
value = instance.CheckInterference(Body1, Body2, CoincidentInterference, Body1InterferedFaceArray, Body2InterferedFaceArray, IntersectedBodyArray)
```

```

System.bool CheckInterference( 
   System.object Body1,
   System.object Body2,
   System.bool CoincidentInterference,
   out System.object Body1InterferedFaceArray,
   out System.object Body2InterferedFaceArray,
   out System.object IntersectedBodyArray
)
```

```

System.bool CheckInterference( 
   System.Object^ Body1,
   System.Object^ Body2,
   System.bool CoincidentInterference,
   [Out] System.Object^ Body1InterferedFaceArray,
   [Out] System.Object^ Body2InterferedFaceArray,
   [Out] System.Object^ IntersectedBodyArray
) 
```

#### Parameters

*Body1*
:   First [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to check for interference

*Body2*
:   Second [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to check for interference

*CoincidentInterference*
:   True to check for coincident interference, false to not

*Body1InterferedFaceArray*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that have interfered from the first body with the second body

*Body2InterferedFaceArray*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that have interfered from the second body with the first body

*IntersectedBodyArray*
:   Array of the interfering [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

#### Return Value

True if successful, false if not

Remarks

Each body must be transformed in the coordinate space of the top-level assembly so that it is positioned the same with respect to the other bodies as it is in assembly space.

To align the two bodies, apply the transformation from [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md) using [IBody2::ApplyTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ApplyTransform.md).

Example

[Check Interference Using IModeler::CheckInterference (VBA)](Check_Interference_using_Modeler_CheckInterference_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::ICheckInterferenceCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount2.md)  
[IAssemblyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.md)  
[IAssemblyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.md)
