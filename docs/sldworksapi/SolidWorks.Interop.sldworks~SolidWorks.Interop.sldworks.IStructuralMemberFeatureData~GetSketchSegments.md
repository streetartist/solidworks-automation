# GetSketchSegments Method (IStructuralMemberFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetSketchSegments`

Gets the sketch segments that define the path of the specified structural member body.
Gets the sketch segments that define the path of the specified structural member body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchSegments( _
   ByVal PBodyIn As Body2 _
) As System.Object
```

```

Dim instance As IStructuralMemberFeatureData
Dim PBodyIn As Body2
Dim value As System.Object
 
value = instance.GetSketchSegments(PBodyIn)
```

```

System.object GetSketchSegments( 
   Body2 PBodyIn
)
```

```

System.Object^ GetSketchSegments( 
   Body2^ PBodyIn
) 
```

#### Parameters

*PBodyIn*
:   [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) whose path sketch segments to get

#### Return Value

Array of [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)s

Example

[Get Structural Member Body Sketch Segments (VBA)](Get_Structural_Member_Body_Sketch_Segments_Example_VB.htm)  
[Get Structural Member Body Sketch Segments (VB.NET)](Get_Structural_Member_Body_Sketch_Segments_Example_VBNET.htm)  
[Get Structural Member Body Sketch Segments (C#)](Get_Structural_Member_Body_Sketch_Segments_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)
