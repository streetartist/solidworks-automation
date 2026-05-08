# ICheckInterferenceCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount2`

Obsolete. Superseded by IModeler::ICheckInterferenceCount3.
Obsolete. Superseded by [IModeler::ICheckInterferenceCount3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICheckInterferenceCount2( _
   ByVal Body1 As Body2, _
   ByVal Body2 As Body2, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef Body1InterferedFaceCount As System.Integer, _
   ByRef Body2InterferedFaceCount As System.Integer, _
   ByRef IntersectedBodyCount As System.Integer _
) As System.Boolean
```

```

Dim instance As IModeler
Dim Body1 As Body2
Dim Body2 As Body2
Dim CoincidentInterference As System.Boolean
Dim Body1InterferedFaceCount As System.Integer
Dim Body2InterferedFaceCount As System.Integer
Dim IntersectedBodyCount As System.Integer
Dim value As System.Boolean
 
value = instance.ICheckInterferenceCount2(Body1, Body2, CoincidentInterference, Body1InterferedFaceCount, Body2InterferedFaceCount, IntersectedBodyCount)
```

```

System.bool ICheckInterferenceCount2( 
   Body2 Body1,
   Body2 Body2,
   System.bool CoincidentInterference,
   out System.int Body1InterferedFaceCount,
   out System.int Body2InterferedFaceCount,
   out System.int IntersectedBodyCount
)
```

```

System.bool ICheckInterferenceCount2( 
   Body2^ Body1,
   Body2^ Body2,
   System.bool CoincidentInterference,
   [Out] System.int Body1InterferedFaceCount,
   [Out] System.int Body2InterferedFaceCount,
   [Out] System.int IntersectedBodyCount
) 
```

#### Parameters

*Body1*
:   First [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to check for interference

*Body2*
:   Second [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to check for interference

*CoincidentInterference*
:   True to check for coincident interference, false to not

*Body1InterferedFaceCount*
:   Number of faces that are interfering that belong to the body passed in the first parameter of this method

*Body2InterferedFaceCount*
:   Number of faces that are interfering that belong to the body passed in the second parameter of this method

*IntersectedBodyCount*
:   Number of intersection bodies produced from this intersection

#### Return Value

True if successful, false if not

Remarks

Call [IModeler::ICheckInterference2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference2.md) after calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CheckInterference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference.md)  
[IAssembyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.md)  
[IAssembyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.md)
