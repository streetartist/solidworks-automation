# ICheckInterferenceCount3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount3`

Checks interference among the specified bodies and returns the number of interferences.
Checks interference among the specified bodies and returns the number of interferences.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICheckInterferenceCount3( _
   ByVal NumOfTargetBodies As System.Integer, _
   ByRef TargetBodies As Body2, _
   ByVal NumOfToolBodies As System.Integer, _
   ByRef ToolBodies As Body2, _
   ByVal Options As System.Integer, _
   ByRef NumBody1InterferedFaceArray As System.Integer, _
   ByRef NumBody2InterferedFaceArray As System.Integer, _
   ByRef NumIntersectedBodyArray As System.Integer _
) As System.Boolean
```

```

Dim instance As IModeler
Dim NumOfTargetBodies As System.Integer
Dim TargetBodies As Body2
Dim NumOfToolBodies As System.Integer
Dim ToolBodies As Body2
Dim Options As System.Integer
Dim NumBody1InterferedFaceArray As System.Integer
Dim NumBody2InterferedFaceArray As System.Integer
Dim NumIntersectedBodyArray As System.Integer
Dim value As System.Boolean
 
value = instance.ICheckInterferenceCount3(NumOfTargetBodies, TargetBodies, NumOfToolBodies, ToolBodies, Options, NumBody1InterferedFaceArray, NumBody2InterferedFaceArray, NumIntersectedBodyArray)
```

```

System.bool ICheckInterferenceCount3( 
   System.int NumOfTargetBodies,
   ref Body2 TargetBodies,
   System.int NumOfToolBodies,
   ref Body2 ToolBodies,
   System.int Options,
   out System.int NumBody1InterferedFaceArray,
   out System.int NumBody2InterferedFaceArray,
   out System.int NumIntersectedBodyArray
)
```

```

System.bool ICheckInterferenceCount3( 
   System.int NumOfTargetBodies,
   Body2^% TargetBodies,
   System.int NumOfToolBodies,
   Body2^% ToolBodies,
   System.int Options,
   [Out] System.int NumBody1InterferedFaceArray,
   [Out] System.int NumBody2InterferedFaceArray,
   [Out] System.int NumIntersectedBodyArray
) 
```

#### Parameters

*NumOfTargetBodies*
:   Number of target bodies

*TargetBodies*
:   Array of target [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*NumOfToolBodies*
:   Number of tool bodies

*ToolBodies*
:   Array of tool [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*Options*
:   Check interference options as defined by [swCheckInterferenceOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCheckInterferenceOption_e.html)

*NumBody1InterferedFaceArray*
:   Number of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that interfered from the first body with the second body

*NumBody2InterferedFaceArray*
:   Number of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that interfered from the second body with the first body

*NumIntersectedBodyArray*
:   Number of interfering [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

Call this method before calling [IModeler::ICheckInterference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.md) to get the size of the arrays for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::ICheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.md)  
[IModeler::CheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.md)  
[IAssemblyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.md)  
[IAssemblyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.md)
