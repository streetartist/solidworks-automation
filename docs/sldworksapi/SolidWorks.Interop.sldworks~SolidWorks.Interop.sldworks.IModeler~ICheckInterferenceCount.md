# ICheckInterferenceCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount`

Obsolete. Superseded by IModeler::ICheckInterferenceCount2.
Obsolete. Superseded by [IModeler::ICheckInterferenceCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICheckInterferenceCount( _
   ByVal Body1 As Body, _
   ByVal Body2 As Body, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef Body1InterferedFaceCount As System.Integer, _
   ByRef Body2InterferedFaceCount As System.Integer, _
   ByRef IntersectedBodyCount As System.Integer _
) As System.Boolean
```

```

Dim instance As IModeler
Dim Body1 As Body
Dim Body2 As Body
Dim CoincidentInterference As System.Boolean
Dim Body1InterferedFaceCount As System.Integer
Dim Body2InterferedFaceCount As System.Integer
Dim IntersectedBodyCount As System.Integer
Dim value As System.Boolean
 
value = instance.ICheckInterferenceCount(Body1, Body2, CoincidentInterference, Body1InterferedFaceCount, Body2InterferedFaceCount, IntersectedBodyCount)
```

```

System.bool ICheckInterferenceCount( 
   Body Body1,
   Body Body2,
   System.bool CoincidentInterference,
   out System.int Body1InterferedFaceCount,
   out System.int Body2InterferedFaceCount,
   out System.int IntersectedBodyCount
)
```

```

System.bool ICheckInterferenceCount( 
   Body^ Body1,
   Body^ Body2,
   System.bool CoincidentInterference,
   [Out] System.int Body1InterferedFaceCount,
   [Out] System.int Body2InterferedFaceCount,
   [Out] System.int IntersectedBodyCount
) 
```

#### Parameters

*Body1*

*Body2*

*CoincidentInterference*

*Body1InterferedFaceCount*

*Body2InterferedFaceCount*

*IntersectedBodyCount*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
