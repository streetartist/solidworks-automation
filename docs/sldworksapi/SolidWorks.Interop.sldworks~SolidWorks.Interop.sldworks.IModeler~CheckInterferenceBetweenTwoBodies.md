# CheckInterferenceBetweenTwoBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterferenceBetweenTwoBodies`

Checks for interference between the specified bodies in an assembly.
Checks for interference between the specified bodies in an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CheckInterferenceBetweenTwoBodies( _
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
 
value = instance.CheckInterferenceBetweenTwoBodies(Body1, Body2, CoincidentInterference, Body1InterferedFaceArray, Body2InterferedFaceArray, IntersectedBodyArray)
```

```

System.bool CheckInterferenceBetweenTwoBodies( 
   System.object Body1,
   System.object Body2,
   System.bool CoincidentInterference,
   out System.object Body1InterferedFaceArray,
   out System.object Body2InterferedFaceArray,
   out System.object IntersectedBodyArray
)
```

```

System.bool CheckInterferenceBetweenTwoBodies( 
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
:   First body in interference detection (see **Remarks**)

*Body2*
:   Second body in interference detection (see **Remarks**)

*CoincidentInterference*
:   True to treat coincidence as interference, false to not

*Body1InterferedFaceArray*
:   Array of faces in the first body that interfered with the second body

*Body2InterferedFaceArray*
:   Array of faces in the second body that interfered with the first body

*IntersectedBodyArray*
:   Array of interfering bodies

#### Return Value

True if successful, false if not

Remarks

Before calling this method, transform Body1 and Body2 to their proper positions in the coordinate space of the top-level assembly:

1. Select the assembly components.
2. Use [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md) to get the transform of each component.
3. Call IComponent2::GetBodies2 for each component.
4. Use [IBody2::ApplyTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ApplyTransform.md) on each body using the transforms in step 2.
5. Specify Body1 and Body1 with the bodies that have been transformed to their correct positions in the assembly.

Example

[Check for Interference Between Two Bodies (VBA)](Check_Interference_Between_Two_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IModeler::CheckInterference3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.md)
