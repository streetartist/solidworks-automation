# Operations2 Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations2`

Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies.
Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Operations2( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBody As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.Operations2(OperationType, ToolBody, ErrorCode)
```

```

System.object Operations2( 
   System.int OperationType,
   System.object ToolBody,
   out System.int ErrorCode
)
```

```

System.Object^ Operations2( 
   System.int OperationType,
   System.Object^ ToolBody,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*OperationType*
:   Operation type as defined in [swBodyOperationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBodyOperationType_e.html)

*ToolBody*
:   Tool body

*ErrorCode*
:   Error indicator as defined in [swBodyOperationError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyOperationError_e.html); returns swBodyOperationNoError if SOLIDWORKS does not generate an error

#### Return Value

Array of pointers to the resulting [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

If the target and tool bodies are the same in geometry, the result body of this method is NULL, and the return value is S\_false.

This method works with two temporary bodies; one is the target and one is the tool. The output is a list of bodies resulting from the operation.

The two temporary bodies used in this function (the Body2 and ToolBody pointers) are invalid once the operation is complete. COM applications should release these two pointers after using this method. If your application needs to maintain these bodies, then you should make a copy of them using [IBody2::Copy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Copy.md) before passing them to this routine.

To perform a [swBodyOperationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBodyOperationType_e.html).SWBODYINTERSECT between a sheet (surface) and a solid body, the sheet body must be the target body.

Use [IBody2::Check3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check3.md) for both bodies before using this method to ensure that both bodies are valid solids. Using this method with invalid bodies can cause unexpected results.

If a non-manifold error is returned, use [IBody2::ResetEdgeTolerances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetEdgeTolerances.md) to visit all of the edges in the body to reset their tolerances. Then use IBody2::Operations2 again.

Example

[Combine Assembly Components into Part (VBA)](Combine_Assembly_Components_into_Part_Example_VB.htm)  
[Create Solid Bodies Using Geometry and Topology (VBA)](Create_Solid_Bodies_using_Geometry_and_Topology_APIs_Example_VB.htm)  
[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)  
[Get Differences Between Parts (VBA)](Get_Differences_Between_Parts_Example_VB.htm)  
[Create and Convert Non-manifold Bodies (C#)](Create_and_Convert_Non-manifold_Bodies_Example_CSharp.htm)  
[Create and Convert Non-manifold Bodies (VB.NET)](Create_and_Convert_Non-manifold_Bodies_Example_VBNET.htm)  
[Create and Convert Non-manifold Bodies (VBA)](Create_and_Convert_Non-manifold_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IOperations2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations2.md)
