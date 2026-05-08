# CheckInterference3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3`

Checks for interferences among the specified bodies in a part.
Checks for interferences among the specified bodies in a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CheckInterference3( _
   ByVal TargetBodies As System.Object, _
   ByVal ToolBodies As System.Object, _
   ByVal Options As System.Integer, _
   ByRef Body1InterferedFaceArray As System.Object, _
   ByRef Body2InterferedFaceArray As System.Object, _
   ByRef IntersectedBodyArray As System.Object _
) As System.Boolean
```

```

Dim instance As IModeler
Dim TargetBodies As System.Object
Dim ToolBodies As System.Object
Dim Options As System.Integer
Dim Body1InterferedFaceArray As System.Object
Dim Body2InterferedFaceArray As System.Object
Dim IntersectedBodyArray As System.Object
Dim value As System.Boolean
 
value = instance.CheckInterference3(TargetBodies, ToolBodies, Options, Body1InterferedFaceArray, Body2InterferedFaceArray, IntersectedBodyArray)
```

```

System.bool CheckInterference3( 
   System.object TargetBodies,
   System.object ToolBodies,
   System.int Options,
   out System.object Body1InterferedFaceArray,
   out System.object Body2InterferedFaceArray,
   out System.object IntersectedBodyArray
)
```

```

System.bool CheckInterference3( 
   System.Object^ TargetBodies,
   System.Object^ ToolBodies,
   System.int Options,
   [Out] System.Object^ Body1InterferedFaceArray,
   [Out] System.Object^ Body2InterferedFaceArray,
   [Out] System.Object^ IntersectedBodyArray
) 
```

#### Parameters

*TargetBodies*
:   Target [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*ToolBodies*
:   Tool [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*Options*
:   Check interference options as defined by [swCheckInterferenceOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCheckInterferenceOption_e.html)

*Body1InterferedFaceArray*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that interfered from the first body with the second body

*Body2InterferedFaceArray*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that interfered from the second body with the first body

*IntersectedBodyArray*
:   Array of interfering [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

#### Return Value

True if an interference exists, false if not

Example

[Check Interference Among Bodies (VBA)](Check_Interference_Among_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::ICheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.md)  
[IModeler::ICheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.md)  
[IAssemblyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.md)  
[IAssemblyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.md)  
[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IModeler::CheckInterferenceBetweenTwoBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterferenceBetweenTwoBodies.md)
