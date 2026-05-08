# MakeSketchBlockFromFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile`

Creates a block definition using the specified file.
Creates a block definition using the specified file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeSketchBlockFromFile( _
   ByVal InsertionPoint As MathPoint, _
   ByVal FileName As System.String, _
   ByVal LinkedToFile As System.Boolean, _
   ByVal Scale As System.Double, _
   ByVal Angle As System.Double _
) As SketchBlockDefinition
```

```

Dim instance As ISketchManager
Dim InsertionPoint As MathPoint
Dim FileName As System.String
Dim LinkedToFile As System.Boolean
Dim Scale As System.Double
Dim Angle As System.Double
Dim value As SketchBlockDefinition
 
value = instance.MakeSketchBlockFromFile(InsertionPoint, FileName, LinkedToFile, Scale, Angle)
```

```

SketchBlockDefinition MakeSketchBlockFromFile( 
   MathPoint InsertionPoint,
   System.string FileName,
   System.bool LinkedToFile,
   System.double Scale,
   System.double Angle
)
```

```

SketchBlockDefinition^ MakeSketchBlockFromFile( 
   MathPoint^ InsertionPoint,
   System.String^ FileName,
   System.bool LinkedToFile,
   System.double Scale,
   System.double Angle
) 
```

#### Parameters

*InsertionPoint*
:   [Insertion point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md), which is a 2D point with z = 0.0, for the block definition

*FileName*
:   Name of the external file to use to create the block definition

*LinkedToFile*
:   True to link the block definition to the file, false to not

*Scale*
:   Scale for the block definition

*Angle*
:   Rotation angle for the block definition

#### Return Value

[Block definition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.md)

Remarks

If the entities of a block are associated with one or more layers and those layers do not already exist in the drawing, then the layers are inserted in the drawing and the associations between the entities of the block and the layers are maintained.

 

The block instance is inserted on the current drawing layer.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::MakeSketchBlockFromSelected Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.md)  
[ISketchManager::MakeSketchBlockFromSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.md)  
[ISketchBlockDefinition::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~FileName.md)  
[ISketchBlockDefinition::LinkToFile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~LinkToFile.md)  
[ISketchBlockDefinition::Save Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~Save.md)
