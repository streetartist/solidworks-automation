# InsertRouteLine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~InsertRouteLine`

Inserts a route line in an explode line sketch or a 3D sketch to indicate component relationships.
Inserts a route line in an explode line sketch or a 3D sketch to indicate component relationships.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertRouteLine( _
   ByVal ItemsToConnect As System.Object, _
   ByVal Reverse As System.Object, _
   ByVal AlternatePath As System.Object, _
   ByVal AlongXYZ As System.Object _
) As System.Boolean
```

```

Dim instance As ISketch
Dim ItemsToConnect As System.Object
Dim Reverse As System.Object
Dim AlternatePath As System.Object
Dim AlongXYZ As System.Object
Dim value As System.Boolean
 
value = instance.InsertRouteLine(ItemsToConnect, Reverse, AlternatePath, AlongXYZ)
```

```

System.bool InsertRouteLine( 
   System.object ItemsToConnect,
   System.object Reverse,
   System.object AlternatePath,
   System.object AlongXYZ
)
```

```

System.bool InsertRouteLine( 
   System.Object^ ItemsToConnect,
   System.Object^ Reverse,
   System.Object^ AlternatePath,
   System.Object^ AlongXYZ
) 
```

#### Parameters

*ItemsToConnect*
:   Array of faces, edges, and vertices to which to connect the route line

*Reverse*
:   Array of Booleans indicating whether to reverse the route line at the corresponding item to connect; true to reverse the direction of the route line, false to not

*AlternatePath*
:   Array of Booleans indicating whether to display an alternate path at the corresponding item to connect; true to display another possible path for the route line, false to not

*AlongXYZ*
:   Array of Booleans indicating whether to create a path parallel to the X, Y, and Z directions from the corresponding item to connect; true to use the X, Y, and Z directions, false to use the shortest route

#### Return Value

True if a route line is inserted, false if not

Remarks

You insert a route line in an [explode line sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertExplodeLineSketch.md).

Example

[Insert Explode Line Sketch and Route Line (VB.NET)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VBNET.htm)  
[Insert Explode Line Sketch and Route Line (VBA)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VB.htm)  
[Insert Explode Line Sketch and Route Line (C#)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[IAssemblyDoc::AutoExplode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.md)
