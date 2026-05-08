# swCommands_e Enumeration

Help ID: `SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swCommands_e`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS API Commands Enumeration | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swCommands_e.html) on this topic. |
| swCommands\_e Enumeration | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All  Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swcommands Namespace](SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands_namespace.md) : swCommands\_e Enumeration |

Visual Basic (Declaration)
  

C#
  

C++/CLI

SOLIDWORKS toolbar and menu commands.

# Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Enum swCommands_e     Inherits System.Enum ``` | |

| C# |  |
| --- | --- |
| ``` public enum swCommands_e : System.Enum ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public enum class swCommands_e : public System.Enum ``` | |

# Members

| Member | Description |
| --- | --- |
| **swCommand\_Border\_Editor** | 3156; valid only for drawings in Edit Sheet Format mode (run swCommands\_e.swCommands\_Edit\_Template before running this command); **Sheet Format toolbar > Automatic Border** |
| **swCommand\_Cartoon\_Shading** | 3170; valid only for assemblies and parts; **View toolbar > View Settings > Cartoon** |
| **swCommand\_ChildReferenceArrow** | 3152; valid only for assemblies; **Assembly toolbar > Dynamic Reference Visualization (Child)** |
| **swCommand\_Component\_Preview\_Window** | 3171; valid only for assemblies; **Assembly toolbar > Component Preview Window** |
| **swCommand\_Delete\_Selected\_BE** | 3158; valid only for drawings in Edit Sheet Format mode while the Automatic Border PropertyManager page is open; selects all items in **Delete List** |
| **swCommand\_Deselect\_All\_Selected\_BE** | 3160; valid only for drawings in Edit Sheet Format mode while the Automatic Border PropertyManager page is open; deselects all selections in **Delete List** |
| **swCommand\_Hide\_Show\_Primary\_Planes** | 3169; valid only for parts; **View toolbar > Hide / Show Primary Planes** |
| **swCommand\_ReferenceArrow\_PopUp** | 3151; valid only for assemblies; **Assembly toolbar > Dynamic Reference Visualization (Parent)** |
| **swCommand\_Restore\_Selected\_BE** | 3159; valid only for drawings in Edit Sheet Format mode while the Automatic Border PropertyManager page is open; restores the selected items in **Delete List** |
| **swCommand\_Sheet\_Format** | 3155; valid only for drawings; **View menu > Toolbars > Sheet Format** |
| **swCommand\_TemporaryFixGroup** | 3162; valid only for assemblies; **Assembly toolbar > Temporary Fix/Group** |
| **swCommands\_2DTo3D** | 509; alternative to swCommands\_Toolbar\_2dto3d; **View menu > Toolbars > 2D to 3D** |
| **swCommands\_2DTo3DCut** | 394; valid only for parts with a single 2D sketch in edit mode; **2D to 3D toolbar > Convert to Cut** |
| **swCommands\_2DTo3DMakeRefsketchBack** | 378; valid only for parts with a single 2D sketch in edit mode; **2D to 3D toolbar > Add to Back Sketch** |
| **swCommands\_2DTo3DMakeRefsketchBottom** | 376; valid only for parts with a single 2D sketch in edit mode; **2D to 3D toolbar > Add to Bottom Sketch** |
| **swCommands\_2DTo3DMakeRefsketchFront** | 373; valid only for parts with a single 2D sketch in edit mode; **2D to 3D toolbar > Add to Front Sketch** |
| **swCommands\_2DTo3DMakeRefsketchLeft** | 377; valid only for parts with a 2D sketch in edit mode; **2D to 3D toolbar > Add to Left Sketch** |
| **swCommands\_2DTo3DMakeRefsketchRight** | 375; valid only for parts with a 2D sketch in edit mode; **2D to 3D toolbar > Add to Right Sketch** |
| **swCommands\_2DTo3DMakeRefsketchTop** | 374; valid only for parts with a 2D sketch in edit mode; **2D to 3D toolbar > Add to Top Sketch** |
| **swCommands\_3DDrawingView** | 548; valid only for drawings; **View toolbar > 3D Drawing View** |
| **swCommands\_3dExperienceDesignEngineer** | 3288; launches 3DEXPERIENCE from SOLIDWORKS Simulation; **Tools toolbar > 3DEXPERIENCE Simulation Connector** |
| **swCommands\_3DPDF\_ADD\_ALL\_3DVIEWS** | 3401; **MBD toolbar > Publish to 3D PDF > Include Primary Views > Select all views** |
| **swCommands\_3dpmi** | 3212; opens the 3D PMI Compare PropertyManager page; **Tools menu > 3D PMI Compare Wizard** |
| **swCommands\_3dPrintValidation** | 3191; opens the 3-D Print Validation PropertyManager page; **View toolbar > 3D Print Validation** |
| **swCommands\_3DSketch** | 89; **Sketch toolbar > 3D Sketch** |
| **swCommands\_3DSketchOnPlane** | 567; valid only for pre-selected planes; **Sketch toolbar  > 3D Sketch On Plane** |
| **swCommands\_3dTexturizeSolidSurface** | 3333; converts solid and surface bodies to texturized graphics bodies; **Features toolbar > Texturize Bodies** |
| **swCommands\_3PointArc** | 80; **Sketch toolbar > 3 Point Arc** |
| **swCommands\_Activate\_And\_Orient\_Annotation\_View** | 2230; valid only for inactive annotation views that are oriented; in the FeatureManager design tree, **Annotations >** *annotation\_view* **RMB menu > Activate and Reorient** |
| **swCommands\_Activate\_Annotation\_View** | 2213; in the FeatureManager design tree, **Annotations >** *annotation\_view* **RMB menu > Activate** |
| **swCommands\_Activate\_Doc\_Or\_Journal** | 2059; in the FeatureManager design tree, **Design Binder  >** *doc\_name* **RMB menu** > **Open** |
| **swCommands\_Activate\_Sheet** | 1206; valid for a selected drawing sheet that is not activated, current, or in edit mode; in the FeatureManager design tree, *sheet* **RMB menu > Activate** |
| **swCommands\_ActivateFlexiblePartComp** | 3418; **Assembly toolbar > Make Part Flexible** |
| **swCommands\_Add\_Bends** | 2290; valid for SOLIDWORKS Electrical add-in and an open assembly with a selected route junction point, opens the Add Bends PropertyManager page; **Electrical toolbar > Add Bends** |
| **swCommands\_Add\_Comment** | 2062; in the FeatureManager design tree, *component\_feature\_or\_sheet* **RMB menu > Comment > Add Comment** |
| **swCommands\_Add\_Configuration** | 1534; in the ConfigurationManager, *configuration\_name* **RMB menu > Add Configuration** or **Add Derived Configuration** |
| **swCommands\_Add\_Constraint\_Alongx** | 2204; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Along X**; when the Line Properties PropertyManager page is open for a selected line in the graphics area, *sel\_line* **RMB context menu > Make AlongX** |
| **swCommands\_Add\_Constraint\_Alongy** | 2205; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Along Y**; when the Line Properties PropertyManager page is open for a selected line in the graphics area, *sel\_line* **RMB context menu > Make AlongY** |
| **swCommands\_Add\_Constraint\_Alongz** | 2206; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Along Z**; when the Line Properties PropertyManager page is open for a selected line in the graphics area, *sel\_line* **RMB context menu > Make AlongZ** |
| **swCommands\_Add\_Constraint\_Atinter** | 1719; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Intersection** |
| **swCommands\_Add\_Constraint\_Atmid** | 1718; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Midpoint** |
| **swCommands\_Add\_Constraint\_Atpierce** | 1724; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Pierce** |
| **swCommands\_Add\_Constraint\_Coinc** | 1720; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Coincident** |
| **swCommands\_Add\_Constraint\_Colinear** | 1712; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Colinear** |
| **swCommands\_Add\_Constraint\_Concent** | 1717; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Concentric** |
| **swCommands\_Add\_Constraint\_Coradial** | 1713; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Coradial** |
| **swCommands\_Add\_Constraint\_Equalcurvature** | 1729; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Equal Curvature** |
| **swCommands\_Add\_Constraint\_Equaltangent** | 1730; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Equal tangent** |
| **swCommands\_Add\_Constraint\_Fix** | 1723; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Fix**; when the Line Properties PropertyManager page is open for a selected line in the graphics area, *sel\_line* **RMB context menu > Make Fixed** |
| **swCommands\_Add\_Constraint\_G3Touch** | 3425; valid only for part sketches in edit mode with a multi-selected arc and spline, adds a continuous curvature variation relation to the selected arc and spline; in the Properties PropertyManager page click **Add Relations > Torsion Continuity**; in the pop-up constraints dialog, click **Make Torsion Continuity** |
| **swCommands\_Add\_Constraint\_Horiz** | 1710; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Horizontal** |
| **swCommands\_Add\_Constraint\_Merge** | 1725; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Merge** |
| **swCommands\_Add\_Constraint\_Normal** | 1726; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Normal** |
| **swCommands\_Add\_Constraint\_Onsurface** | 2217; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > On Surface** |
| **swCommands\_Add\_Constraint\_Parallel** | 1715; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Parallel** |
| **swCommands\_Add\_Constraint\_Parallelyz** | 1727; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Parallel YZ** |
| **swCommands\_Add\_Constraint\_Parallelzx** | 1728; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Parallel ZX** |
| **swCommands\_Add\_Constraint\_Perp** | 1714; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Perpendicular** |
| **swCommands\_Add\_Constraint\_Planar\_Offset** | 3003; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Offset** |
| **swCommands\_Add\_Constraint\_SameCurvelen** | 3153; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Equal Arc/Spline** |
| **swCommands\_Add\_Constraint\_Samelen** | 1721; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Equal** |
| **swCommands\_Add\_Constraint\_Sym** | 1722; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Symmetric** |
| **swCommands\_Add\_Constraint\_Tanface** | 1731; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Tangent to Face** |
| **swCommands\_Add\_Constraint\_Tang** | 1716; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Tangent** |
| **swCommands\_Add\_Constraint\_Traction** | 1732; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Traction** |
| **swCommands\_Add\_Constraint\_Vert** | 1711; accessible only for part sketches in edit mode where this relation is possible; click **Sketch toolbar >** **Relations > Add Relation** or **Tools menu > Relations > Add**; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click **Add Relations > Vertical** |
| **swCommands\_Add\_Coverings** | 2286; valid for the SOLIDWORKS Routing add-in and a selected route segment in an open routing assembly, opens the Covering PropertyManager page**; Routing Tools** **toolbar** **> Covering** |
| **swCommands\_Add\_Derived\_Configuration** | 2461; in the ConfigurationManager, *configuration\_name* **RMB menu > Add Derived Configuration** |
| **swCommands\_Add\_Feature\_Dims** | 1552; valid for dimensioned parts; in FeatureManager design tree, f*eature\_name* **RMB menu > Show All Dimensions** |
| **swCommands\_Add\_Fitting** | 2285; valid for the SOLIDWORKS Routing add-in and a routing assembly**;** **Piping** or **Flexible Tubing** or**User Defined** **toolbar** **> Add Fitting** |
| **swCommands\_Add\_OverallDim\_To\_ChainDim** | 3424; valid only ifan overall chain dimension does not already exist for the chain dimension set, automatically adds an overall dimension between a selected dimension in the chain dimension set and the dimension(s) that are farthest from the selection, in both directions if applicable; **RMB menu > Add Overall** |
| **swCommands\_Add\_Part\_Block** | 2823; valid for blocks created in assembly layouts; in the FeatureManager design tree, *block\_name* **RMB menu > Make Part from Block** |
| **swCommands\_Add\_Slope** | 3103; valid for the SOLIDWORKS Routing add-in and a piping assembly, opens the Pipe Slope PropertyManager page**; Piping** **toolbar** **> Add Slope** |
| **swCommands\_Add\_Split\_Feat\_To\_Asm** | 1818; valid only for parts with a split feature; **Insert menu > Features > Create Assembly** |
| **swCommands\_Add\_To\_Bookmark** | 3514; valid only in SOLIDWORKS Connected, adds the current file to the bookmark folder; **Lifecycle and Collaboration toolbar > Bookmarks > Add to Bookmark** |
| **swCommands\_Add\_to\_CMarkSet** | 3131; valid only for drawings with a center mark set; in the graphics view, *center\_mark* **RMB menu >Add to Center Mark Set** |
| **swCommands\_Add\_To\_Palette** | 2171; valid for parts with a selected geometric tolerance symbol, opens the Add to Library PropertyManager page; in the graphics area, *geo\_tol* **RMB menu > Add to Library**; also valid for assemblies; in the FeatureManager design tree, *component\_name* **RMB menu > Add to Library** |
| **swCommands\_Add\_To\_Recent\_Bookmark** | 3525; valid only in SOLIDWORKS Connected, adds selected files and components to your recent bookmarks; **Lifecycle and Collaboration toolbar > Bookmarks > Add to Recent Bookmark** |
| **swCommands\_AddCurvatureControl** | 416; valid only for 2D spline sketches; **Spline Tools toolbar > Add Curvature Control** |
| **swCommands\_AddRelation** | 71; valid for sketches in edit mode; **Dimensions/Relations toolbar > Add Relation** |
| **swCommands\_AddRemove** | 515; valid for blocks in edit mode; **Layout** or **Blocks toolbar >Add/Remove** |
| **swCommands\_AddTangencyControl** | 415; valid only for 2D and 3D spline sketches; **Spline Tools toolbar > Add Tangency Control** |
| **swCommands\_AddTo\_Chain\_Dimension** | 3406; valid for a selected dimension in a chain dimension set; **RMB menu > Add to Chain** |
| **swCommands\_AdvancedHoleWizard** | 3172; opens the Hole Specification PropertyManager page; **Features toolbar > Advanced Hole Wizard** |
| **swCommands\_AdvancedStructuralMember** | 3335;  creates a structural member feature by sweeping pre-defined profiles along user-defined paths; **Structure System toolbar > Create Structure System** |
| **swCommands\_Align** | 474; alternative to swCommands\_Toolbar\_Align; **View menu > Toolbars > Align** |
| **swCommands\_Align\_Horz** | 1511; valid for drawing view items; in the graphics area, *view\_item* **RMB menu > Alignment > Align Horizontal by Origin** |
| **swCommands\_Align\_Horz\_By\_Center** | 695; valid for drawing view items; in the graphics area, *view\_item* **RMB menu > Alignment > Align Horizontal by Center** |
| **swCommands\_Align\_Ordinate** | 1505; valid for drawings of circles or arcs with angular running dimensions; in the graphics area, *angular\_running\_dimensi*on **RMB menu > Display Options > Align Running Dimension** |
| **swCommands\_Align\_Vert** | 1512; valid for drawing view items; in the graphics area, *view\_item* **RMB menu > Alignment > Align Vertical by Origin** |
| **swCommands\_Align\_Vert\_By\_Center** | 694; valid for drawing view items; in the graphics area, *view\_item* **RMB menu > Alignment > Align Vertical by Center** |
| **swCommands\_Align\_With\_Assy\_Origin** | 2274; valid in assemblies after *component* **RMB menu > Move with Triad** command; in the graphics area, *triad\_center\_ball* **RMB menu > Align with Assembly Origin** |
| **swCommands\_Align\_With\_Comp\_Origin** | 2273; valid in assemblies after *component* **RMB menu > Move with Triad** command; in the graphics area, *triad\_center\_ball* **RMB menu > Align with Component Origin** |
| **swCommands\_Align\_With\_Selection** | 2279; valid after *component* **RMB menu > Move with Triad** command in assembly; in the graphics area, *triad\_ball\_arrow* **RMB menu > Align with selection** |
| **swCommands\_AlignBetweenLines** | 579; valid in drawings where a dimension or annotation and two vertical or horizontal lines are selected; **Align toolbar > Align Between Lines** |
| **swCommands\_AlignBottom** | 310; valid for multi-selected annotations or dimensions; **Align** **toolbar > Align Bottom** |
| **swCommands\_AlignCollinearRadial** | 145; valid for multi-selected dimensions; **Align toolbar > Align Collinear/Radial** |
| **swCommands\_AlignedSectionView** | 108; valid for parts and assemblies; in the Section View Assist PropertyManager page; **Cutting Line > Aligned** |
| **swCommands\_AlignHorizontal** | 314; valid for multi-selected annotations or dimensions; **Align** **toolbar > Align Horizontal** |
| **swCommands\_AlignLeft** | 389; valid for selected text; **Formatting toolbar > Align Left** |
| **swCommands\_AlignParallelConcentric** | 146; valid for multi-selected dimensions; **Align toolbar > Align Parallel/Concentric** |
| **swCommands\_AlignRight** | 388; valid for selected text; **Formatting toolbar > Align Right** |
| **swCommands\_AlignSketch** | 379; valid for parts; **2D To 3D toolbar > Align Sketch** or **Tools > Sketch Tools > Align > Sketch** |
| **swCommands\_AlignTop** | 309; valid for multi-selected annotations or dimensions; **Align** **toolbar > Align Top** |
| **swCommands\_AlignVertical** | 315; valid for multi-selected annotations or dimensions; **Align toolbar > Align Vertical** |
| **swCommands\_AlternatePositionView** | 357; valid for a selected drawing sheet with alternate position views; **Drawing toolbar > Alternate Position View** |
| **swCommands\_AlternativeHandwrittenDim\_0** | 3388; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the first of ten alternative values that were calculated from InkAnalysis handwriting recognition; **RMB dimension context menu >** *alternative\_value\_1* |
| **swCommands\_AlternativeHandwrittenDim\_1** | 3389; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the second of ten alternative values that were calculated from InkAnalysis handwriting recognition; **RMB dimension context menu >** *alternative\_value\_2* |
| **swCommands\_AlternativeHandwrittenDim\_2** | 3390; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the third of ten alternative values that were calculated from InkAnalysis handwriting recognition; **RMB dimension context menu >** *alternative\_value\_3* |
| **swCommands\_AlternativeHandwrittenDim\_3** | 3391; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the fourth of ten alternative values that were calculated from InkAnalysis handwriting recognition; **RMB dimension context menu >** *alternative\_value\_4* |
| **swCommands\_AlternativeHandwrittenDim\_4** | 3392; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the fifth of ten alternative values that were calculated from InkAnalysis handwriting recognition; **RMB dimension context menu >** *alternative\_value\_5* |
| **swCommands\_AlternativeHandwrittenDim\_5** | 3393; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the sixth of ten alternative values that were calculated from InkAnalysis handwriting recognition; **RMB dimension context menu >** *alternative\_value\_6* |
| **swCommands\_AlternativeHandwrittenDim\_6** | 3394; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the seventh of ten alternative values that were calculated from InkAnalysis handwriting recognition; **RMB dimension context menu >** *alternative\_value\_7* |
| **swCommands\_AlternativeHandwrittenDim\_7** | 3395; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the eighth of ten alternative values that were calculated from InkAnalysis handwriting recognition; **RMB dimension context menu >** *alternative\_value\_8* |
| **swCommands\_AlternativeHandwrittenDim\_8** | 3396; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the ninth of ten alternative values that were calculated from InkAnalysis handwriting recognition; **RMB dimension context menu >** *alternative\_value\_9* |
| **swCommands\_AlternativeHandwrittenDim\_9** | 3397; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the tenth of ten alternative values that were calculated from InkAnalysis handwriting recognition; **RMB dimension context menu >** *alternative\_value\_10* |
| **swCommands\_Ambient\_Occlusion** | 3030; valid only if  RealView Graphics is enabled in parts and assemblies; **View toolbar > View Settings > Ambient Occlusion** |
| **swCommands\_AnalysistoolsDraftAnalysis** | 2885; valid for assemblies with a mold base and design parts; **Mold Tools toolbar > Draft Analysis** |
| **swCommands\_AnalysistoolsPartingLineAnalysis** | 2887; valid for assemblies with a mold base and design parts; **Mold Tools toolbar > Parting Line Analysis** |
| **swCommands\_AnalysistoolsUndercutAnalysis** | 2886; valid for assemblies with a mold base and design parts; **Mold Tools toolbar > Undercut Analysis** |
| **swCommands\_AngleSnap** | 536; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; **Quick Snaps toolbar > Angle Snap** |
| **swCommands\_AngularOrdinateDimension** | 3068; valid only for arcs in drawing views; **Dimensions/Relations toolbar > Angular Running Dimension** |
| **swCommands\_Anim\_Custom\_Msg\_Display\_Camera\_By\_Name** | 2353; valid only in the context of Motion Studies for a selected Orientation and Camera View bar key; in the Motion Study gantt chart, *orientation\_and\_camera\_views\_time\_bar\_key* **RMB menu > View Orientation >***camera\_view\_name* |
| **swCommands\_Anim\_Custom\_Msg\_Display\_Vw\_By\_Name** | 2352; valid only in the context of Motion Studies for a selected Orientation and Camera View bar key; in the Motion Study gantt chart, *orientation\_and\_camera\_views\_time\_bar\_key* **RMB menu > View Orientation >***view\_name* |
| **swCommands\_Anim\_Edit\_Dim** | 2798; valid only in the context of Motion Studies; in the MotionManager tree, **MateGroup1 >** *mate\_name* **>** *mate\_dimension* **RMB menu > Edit Dimension** |
| **swCommands\_Anim\_Lock\_Viewpoint** | 2644; valid only in the context of Motion Studies; in the MotionManager tree, **Orientation and Camera Views RMB menu > Disable View Key Creation** |
| **swCommands\_Anim\_Suppress\_Viewpoint** | 2643; valid only in the context of Motion Studies; in the MotionManager tree, **Orientation and Camera Views RMB menu > Disable Playback of View Keys** |
| **swCommands\_Anim\_View\_Back** | 2344; valid only in the context of Motion Studies for a selected Orientation and Camera View time bar; in the gantt chart, *orientation\_and\_camera\_views\_time\_bar* **RMB menu > View Orientation > Back** |
| **swCommands\_Anim\_View\_Bottom** | 2348 valid only in the context of Motion Studies for a selected Orientation and Camera View time bar; in the gantt chart, *orientation\_and\_camera\_views\_time\_bar* **RMB menu > View Orientation > Bottom** |
| **swCommands\_Anim\_View\_Camera** | 2354; valid only in the context of Motion Studies with a camera view and for a selected Orientation and Camera View time bar; in the Motion Study gantt chart, *orientation\_and\_camera\_views\_time\_bar* **RMB > Camera View** |
| **swCommands\_Anim\_View\_Dimetric** | 2351; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, *orientation\_and\_camera\_views\_time\_bar* **RMB menu > View Orientation > Dimetric** |
| **swCommands\_Anim\_View\_Front** | 2343; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, *orientation\_and\_camera\_views\_time\_bar* **RMB menu > View Orientation > Front** |
| **swCommands\_Anim\_View\_Isometric** | 2349; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, *orientation\_and\_camera\_views\_time\_bar* **RMB menu > View Orientation > Isometric** |
| **swCommands\_Anim\_View\_Left** | 2345; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, *orientation\_and\_camera\_views\_time\_bar* **RMB menu > View Orientation > Left** |
| **swCommands\_Anim\_View\_Right** | 2346; valid only in the context of Motion Studies and a selected Orientation and Camera View row; in the gantt chart, *orientation\_and\_camera\_views\_time\_bar* **RMB menu > View Orientation > Right** |
| **swCommands\_Anim\_View\_Top** | 2347; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, *orientation\_and\_camera\_views\_time\_bar* **RMB menu > View Orientation > Top** |
| **swCommands\_Anim\_View\_Trimetric** | 2350; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, *orientation\_and\_camera\_views\_time\_bar* **RMB menu > View Orientation > Trimetric** |
| **swCommands\_Animation\_CancelSolver** | 2929; **Motion Study tab RMB menu > Cancel Solver Status** |
| **swCommands\_Animation\_Delete** | 2144; **Motion Study tab RMB menu > Delete** |
| **swCommands\_Animation\_Duplicate** | 2827; **Motion Study tab RMB menu > Duplicate** |
| **swCommands\_Animation\_Ff** | 1962; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Fast Forward** |
| **swCommands\_Animation\_Goto\_End** | 1963; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **End** |
| **swCommands\_Animation\_Goto\_Start** | 1959; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Start** |
| **swCommands\_Animation\_MoveCurTime** | 2918; valid only in the context of Motion Studies; opens the Edit Time dialog; in Motion Study gantt chart, **RMB menu > Move Time Bar** |
| **swCommands\_Animation\_New** | 2142; valid for assemblies; **Assembly toolbar > New Motion Study** |
| **swCommands\_Animation\_Pause** | 1964; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB menu > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Pause** |
| **swCommands\_Animation\_Play** | 1961; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB menu > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Play** |
| **swCommands\_Animation\_Play\_Fast** | 1971; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB menu > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Fast Play** |
| **swCommands\_Animation\_Play\_From\_Start** | 657; **MotionManager toolbar > Play from Start** |
| **swCommands\_Animation\_Play\_Loop** | 1968; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB menu > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Playback Mode: Loop** |
| **swCommands\_Animation\_Play\_Normal** | 1967; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB menu > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Playback Mode: Normal** |
| **swCommands\_Animation\_Play\_Reciprocate** | 1969; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB menu > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Playback Mode: Reciprocate** |
| **swCommands\_Animation\_Play\_Slow** | 1970; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB menu > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Slow Play** |
| **swCommands\_Animation\_Record** | 1966; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB menu > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Save Animation** |
| **swCommands\_Animation\_Rename** | 2143; **Motion Study tab RMB menu > Rename** |
| **swCommands\_Animation\_Rewind** | 1960; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB menu > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Rewind** |
| **swCommands\_Animation\_SolverStatus** | 2930; **Motion Study tab RMB menu > Show Solver Status** |
| **swCommands\_Animation\_Stop** | 1965; valid only when exploding a view or collapsing an exploded view; **Configurations tab >** *exploded\_view\_name* **RMB menu > Animate Explode/Collapse**; in Animation Controller Pop-Up Toolbar, **Stop** |
| **swCommands\_Animation\_Wizard** | 659; valid only in the context of Motion Studies, opens the Select an Animation Type dialog; in a Motion Study gantt chart, **RMB menu > Animation Wizard;** also available on the MotionManager toolbar |
| **swCommands\_AnimEditTime\_Dlg\_Cancel** | 2920; valid only in the context of Motion Studies; in the Motion Study gantt chart **RMB menu > Move Time Bar > Edit Time dialog > Cancel** |
| **swCommands\_AnimEditTime\_Dlg\_Increment** | 2923; valid only in the context of Motion Studies; in the Motion Study gantt chart **RMB menu > Move Time Bar > Edit Time dialog >** **Spin Increment** |
| **swCommands\_AnimEditTime\_Dlg\_Ok** | 2919; valid only in the context of Motion Studies; in the Motion Study gantt chart **RMB menu > Move Time Bar > Edit Time dialog >** **OK** |
| **swCommands\_AnimEditTime\_Dlg\_SetOffset** | 2922; valid only in the context of Motion Studies; in the Motion Study gantt chart **RMB menu > Move Time Bar > Edit Time dialog >****Offset** |
| **swCommands\_AnimEditTime\_Dlg\_SetTime** | 2921; valid only in the context of Motion Studies; in the Motion Study gantt chart **RMB menu > Move Time Bar > Edit Time dialog >** **Exact Time** |
| **swCommands\_Animkey\_Clear** | 2137; valid only in the context of Motion Studies for a selected gantt chart time bar key; in the Motion Study gantt chart, *orientation\_and\_camera\_views\_time\_bar\_key* **RMB > Delete** |
| **swCommands\_Animkey\_Copy** | 2135; valid only in the context of Motion Studies for a selected gantt chart time bar key; in Motion Study gantt chart, *time\_bar\_key* **RMB menu > Copy** |
| **swCommands\_Animkey\_Cut** | 2134; valid only in the context of Motion Studies for a selected gantt chart time bar key; in the Motion Study gantt chart, *time\_bar\_key* **RMB menu > Cut** |
| **swCommands\_Animkey\_EditTime** | 2917; valid only in the context of Motion Studies for a selected gantt chart time bar key, opens the Edit Time dialog; in the Motion Study gantt chart, *time\_bar\_key* **RMB menu > Edit Key Point Time** |
| **swCommands\_Animkey\_Interp\_Easein\_Sin** | 2161; valid only in the context of Motion Studies for a selected gantt chart time bar key at position B; in the Motion Study gantt chart, *time\_bar\_key\_pos\_B* **RMB menu > Interpolation mode > Ease in** |
| **swCommands\_Animkey\_Interp\_Easeinout\_Sin** | 2163; valid only in the context of Motion Studies for a selected gantt chart time bar key at position B; in the Motion Study gantt chart, *time\_bar\_key\_pos\_B* **RMB menu > Interpolation mode >** **Ease in/Ease out** |
| **swCommands\_Animkey\_Interp\_Easeout\_Sin** | 2162; valid only in the context of Motion Studies for a selected gantt chart time bar key at position B; in the Motion Study gantt chart, *time\_bar\_key\_pos\_B* **RMB menu > Interpolation mode >** **Ease out** |
| **swCommands\_Animkey\_Interp\_Linear** | 2157; valid only in the context of Motion Studies for a selected gantt chart time bar key at position B; in the Motion Study gantt chart, *time\_bar\_key\_pos\_B* **RMB menu > Interpolation mode >** **Linear** |
| **swCommands\_Animkey\_Interp\_Step\_End** | 2156; valid only in the context of Motion Studies for a selected gantt chart time bar key at position B; in the Motion Study gantt chart, *time\_bar\_key\_pos\_B* **RMB menu > Interpolation mode >** **Snap** |
| **swCommands\_Animkey\_Paste** | 2136; valid only in the context of Motion Studies for a copied gantt chart time bar key; in the Motion Study gantt chart, *time\_bar\_key* **RMB menu > Paste** |
| **swCommands\_Animkey\_Place** | 2140; valid only in the context of Motion Studies; in the Motion Study gantt chart, **RMB menu > Place Key** |
| **swCommands\_Animkey\_Replace** | 2141; valid only in the context of Motion Studies for a selected gantt chart time bar key; in the Motion Study gantt chart, *time\_bar\_key* **RMB menu > Replace Key** |
| **swCommands\_Animkey\_Reverse\_Path** | 2150; valid only in the context of Motion Studies for a selected assembly gantt chart time bar key; in the Motion Study gantt chart, *time\_bar\_key* **RMB menu > Reverse Path** |
| **swCommands\_Animkey\_Select\_All** | 2138; valid only in the context of Motion Studies; in the Motion Study gantt chart, **RMB menu > Select All** |
| **swCommands\_Animkey\_Suppress** | 2155; valid only in the context of Motion Studies for a selected gantt chart time bar key; in the Motion Study gantt chart, *time\_bar\_key* **RMB > Suppress Key** |
| **swCommands\_AnimMateSuppress** | 2932; valid only in the context of Motion Studies for a selected mate; in the Motion Study gantt chart, *mate\_line\_gantt\_time\_bar* **RMB menu > Suppress** |
| **swCommands\_AnimMateUnsuppress** | 2933; valid only in the context of Motion Studies for a selected mate; in the Motion Study gantt chart, *mate\_line\_gantt\_time\_bar* **RMB menu >** **Unsuppress** |
| **swCommands\_Ann\_Feat\_Dim** | 1550; in the FeatureManager design tree, **Annotations folder RMB menu > Show Feature Dimensions** |
| **swCommands\_Ann\_Ref\_Dim** | 1551; in the FeatureManager design tree, **Annotations folder RMB menu > Show Reference Dimensions** |
| **swCommands\_Ann\_Show** | 1549; in the FeatureManager design tree, **Annotations folder RMB menu > Display Annotations** |
| **swCommands\_Annotation\_View\_Create** | 2210; in the FeatureManager design tree, **Annotations folder RMB menu > Insert Annotation View** |
| **swCommands\_Annotation\_View\_Hide** | 2233; in the FeatureManager design tree, **Annotations >** *annotation\_view* **RMB menu > Hide** |
| **swCommands\_Annotation\_View\_Show** | 2232; in the FeatureManager design tree, **Annotations >** *annotation\_view* **RMB menu > Show** |
| **swCommands\_AnnotationAlignLeft** | 307; valid for multi-selected annotations; **Align toolbar > Align Left** |
| **swCommands\_AnnotationAlignRight** | 308; valid for multi-selected annotations; **Align toolbar > Align Right** |
| **swCommands\_Annotations** | 475; alternative to swCommands\_Toolbar\_Annotation; **View menu > Toolbars > Annotation** |
| **swCommands\_Api\_Help\_Contents** | 833; **? menu > API Help** |
| **swCommands\_App\_Exit** | 2825; **File menu > Exit** |
| **swCommands\_App\_Servicepacks** | 1233; **? menu > Check for Updates** |
| **swCommands\_Apply** | 696; dialog resource **Apply** |
| **swCommands\_AreaHatchFill** | 384; valid only for a selected face or closed sketch profile in a drawing; **Annotations toolbar > Area Hatch/Fill** |
| **swCommands\_Asm\_Cir\_Feat\_Pattern** | 1376; valid for a selected assembly hole or cut and a selected axis about which to create the circular pattern, opens the Circular Pattern PropertyManager page; **Insert menu > Assembly Feature > Circular Pattern** |
| **swCommands\_Asm\_Feat\_Chamfer** | 2957; valid for a selected assembly feature, opens the Chamfer PropertyManager page; **Insert menu > Assembly Feature > Chamfer** |
| **swCommands\_Asm\_Feat\_Cut\_Extr** | 1001; valid for a selected location on an assembly, opens the Extrude PropertyManager page; **Insert menu > Assembly Feature > Cut > Extrude** |
| **swCommands\_Asm\_Feat\_Cut\_Revolve** | 1002; valid for a selected location on an assembly, opens the Revolve PropertyManager page; **Insert menu > Assembly Feature > Cut > Revolve** |
| **swCommands\_Asm\_Feat\_Cut\_Sweep** | 2958; valid for assemblies, opens the Cut-Sweep PropertyManager page; **Insert menu > Assembly Feature > Cut > Sweep** |
| **swCommands\_Asm\_Feat\_Fillet** | 2956; valid for a selected assembly feature, opens the Fillet PropertyManager page; **Insert menu > Assembly Feature > Fillet** |
| **swCommands\_Asm\_Feature\_Hole** | 1003; valid for a selected location on an assembly; **Insert menu > Assembly Feature > Hole > Simple** |
| **swCommands\_Asm\_Lin\_Feat\_Pattern** | 1375; valid for a selected assembly hole or cut and a selected axis for the pattern direction, opens the Linear Pattern PropertyManager page; **Insert menu > Assembly Feature > Linear Pattern** |
| **swCommands\_Asm\_Sketch\_Feat\_Pattern** | 1382; valid for a selected assembly hole or cut, opens the Sketch Driven Pattern PropertyManager page; **Insert menu > Assembly Feature > Sketch Driven Pattern** |
| **swCommands\_Asm\_Table\_Feat\_Pattern** | 1380; valid for a selected assembly hole or cut, opens the Table Driven Pattern dialog; **Insert menu > Assembly Feature > Table Driven Pattern** |
| **swCommands\_Assemblies** | 476; alternative to swCommands\_Toolbar\_Assembly; **View menu > Toolbars > Assembly** |
| **swCommands\_Assembly\_Stats** | 1215; valid for assemblies; **Assembly toolbar > Performance Evaluation** |
| **swCommands\_AssemblyTransparency** | 3; valid only for assemblies that have one or more components in edit mode; in the graphics area, click **RMB menu > Assembly Transparency** |
| **swCommands\_Asset\_Publish** | 3215; opens the Asset Publisher PropertyManager page; **Tools menu or toolbar > Asset Publisher** |
| **swCommands\_Assign\_Smart\_Fastener** | 2452; valid only for Toolbox add-ins and assemblies and only when editing a Smart Fastener grouping, opens the Smart Fastener dialog; in the Smart Fasteners PropertyManager page, **Results > Group1 > Series1** **RMB menu > Change fastener type** |
| **swCommands\_Attach\_Dimensions** | 986; valid only for drawings; **Tools menu > Dimensions > Attach Dimensions** |
| **swCommands\_Auto\_Ann\_View\_Generate** | 2223; in the FeatureManager design tree, **Annotations folder RMB menu > Automatically Place into Annotation Views** |
| **swCommands\_Auto\_Dimension\_Toggle** | 3026; valid for an open sketch with an active sketch tool; **Sketch toolbar > Add Dimension** |
| **swCommands\_Auto\_Jog** | 639; valid for a selected ordinate dimension; in the graphics area, ord\_dim RMB menu > Display Options > Re-Jog Ordinate |
| **swCommands\_Auto\_Size** | 1702; valid for a reference plane that is re-sized; in the graphics area *ref\_plane* **RMB menu > Autosize** |
| **swCommands\_AutoArrangeDimension** | 2976; valid for multi-selected annotations or dimensions; **Align toolbar > Auto Arrange Dimensions** |
| **swCommands\_AutoBalloon** | 447; valid for drawings; **Annotations toolbar > Auto Balloon** |
| **swCommands\_AutoExplodeLine** | 3296; valid for assemblies, opens Smart Explode Lines PropertyManager to insert or edit smart explode lines for a selected explode view; **Assembly toolbar > Insert/Edit Smart Explode Lines** |
| **swCommands\_AutoGenerateDrawing** | 3536; valid for parts and assemblies, auto-generates a new drawing from the model; **File menu > Auto-Generate Drawing** |
| **swCommands\_Autoinfer\_Toggle** | 1301; valid for drawings; **Tools menu > Sketch Settings > Enable Snapping** |
| **swCommands\_Automatic\_Cutlist** | 2601; valid for a selected body folder or cut list folder; in the FeatureManager design tree, *folder* **RMB menu > Create Cut Lists Automatically** |
| **swCommands\_AutomaticRelations** | 52; **Dimensions/Relations toolbar > Automatic Relations** |
| **swCommands\_AutomaticUpdateCutlists** | 3122; valid for a cut list folder that has enabled Create Cut Lists Automatically; in the FeatureManager design tree, *folder* **RMB menu > Update Automatically** |
| **swCommands\_AutoRepair\_Mates** | 3510; Auto repairs mates in a model that is in resolved or lightweight mode; right-click on the Mates root folder and click Auto Repair. |
| **swCommands\_AutoRepair\_Pattern** | 3520; Auto repairs a missing Direction 1 or Direction 2 selection in a linear pattern; Right-click the pattern feature in the FeatureManager design tree and click **Auto Repair** in the pattern context menu |
| **swCommands\_Autosolve\_Toggle** | 997; valid for drawings; **Tools menu > Sketch Settings > Automatic Solve** |
| **swCommands\_Auxiliary** | 391; valid for part documents with a single 2D sketch in edit mode; **2D to 3D toolbar > Auxiliary Sketch** |
| **swCommands\_AuxiliaryView** | 33; valid for drawings; **Drawing toolbar > Auxiliary View** |
| **swCommands\_Axis** | 22; valid for parts; **Reference Geometry toolbar > Axis** or **Features toolbar > Reference Geometry > Axis** |
| **swCommands\_Back** | 162; **View toolbar > View Orientation > Back** |
| **swCommands\_Backward** | 1616; **palette toolbar >** **Back** |
| **swCommands\_Balloon** | 37; **Annotations toolbar > Balloon** |
| **swCommands\_BaseFlangeTab** | 320; valid for sheet metal parts; **Sheet Metal toolbar > Base Flange/Tab** |
| **swCommands\_BaselineDimension** | 81; valid only for drawings; **Dimensions/Relations toolbar > Baseline Dimension** |
| **swCommands\_BendTable** | 3010; valid only for selected flat-pattern views in drawings; **Table toolbar > Bend Table** or **Insert > Tables > Bend Table** |
| **swCommands\_BillOfMaterials** | 88; valid for drawings; **Table toolbar > Bill of Materials** |
| **swCommands\_Blank\_Atom\_Body** | 1026; in the FeatureManager design tree, click *body\_folder* **RMB context toolbar > Hide** |
| **swCommands\_Blank\_Atom\_Body2** | 2730; valid for a part with a solid or surface body; in the FeatureManager design tree, *body\_folder* **>** *body* **RMB context toolbar > Hide** |
| **swCommands\_Blank\_Grid\_Comp** | 3000; valid for a part or assembly with the GridSystem PropertyManager page open and the grid feature component visible; in the graphics area, **RMB menu > Hide** |
| **swCommands\_Blank\_Origin\_Sketch** | 2468; valid for a visible profile sketch; in the graphics area, *prof\_sketch* **RMB menu > Hide** |
| **swCommands\_Blank\_Part\_Body** | 901; valid for a selected face of an atom feature in an assembly; in the graphics area, *sel\_face* **RMB menu > Hide Solid Body** |
| **swCommands\_Blank\_Pic\_Feat** | 2485; valid for a selected visible picture feature object; in the graphics area, *pic\_feat* **RMB menu > Hide** |
| **swCommands\_Blank\_Refgeom** | 895; valid for a selected reference geometry; in the FeatureManager design tree, *ref\_geom* **RMB menu > Hide** |
| **swCommands\_Blank\_Sketch** | 954; valid for a selected drawing sketch; in the graphics area, *sketch* **RMB menu > Hide** |
| **swCommands\_Blocks** | 557; alternative to swCommands\_Toolbar\_Sketch\_Group; **View menu > Toolbars > Blocks** |
| **swCommands\_Body\_Color** | 648; in the FeatureManager design tree, *body\_folder* **RMB menu > Appearance > Sketch/Curve Color** |
| **swCommands\_Body\_Properties** | 2519; in the FeatureManager design tree, *body\_name* **RMB menu > Body Properties** |
| **swCommands\_Body\_RV\_Appearance** | 2896; in the FeatureManager design tree, *body\_folder* **RMB menu > Appearance** |
| **swCommands\_Body\_Texture** | 650; valid for a selected component in an assembly, opens the Texture PropertyManager page |
| **swCommands\_BodyComparison** | 3411; valid for selected bodies, displays color comparison; **View toolbar > Body Compare** |
| **swCommands\_Bold** | 147; valid for selected text; **Formatting toolbar > Bold** |
| **swCommands\_Bold\_Menu\_Title** | 2359; adds the bold font style to a selected item in RMB menus |
| **swCommands\_Bom\_Open\_Comp\_File** | 2557; valid for a selected row in a drawing BOM table; *BOM\_table\_row* **RMB menu > Open *comp\_file*** |
| **swCommands\_Bom\_Open\_Draw\_File** | 3502; valid for a selected row in a drawing BOM table; *BOM\_table\_row* **RMB menu > Open Drawing** |
| **swCommands\_Bom\_Viewtable** | 1302; valid for a drawing view Excel-based BOM; E*xcel\_based\_bom* **RMB menu > Edit** |
| **swCommands\_Bottom** | 166; **View toolbar > View Orientation > Bottom** |
| **swCommands\_Bottom\_Left** | 933; valid for a selected Excel-based BOM in a drawing view; *Excel\_BOM* **RMB menu > Anchor > Bottom Left** |
| **swCommands\_Bottom\_Right** | 930; valid for a selected Excel-based BOM in a drawing view; *Excel\_BOM* **RMB menu > Anchor > Bottom Right** |
| **swCommands\_Break\_Alignment** | 1510; valid only for aligned drawing view items; *view\_item* **RMB menu > Alignment > Break Alignment** |
| **swCommands\_Break\_Dim\_Align** | 1562; valid for a selected drawing dimension to which Align Collinear/Radial has been applied; in the graphics area, *aligned\_dim* **RMB menu >** **Break Alignment** |
| **swCommands\_Break\_View** | 1519; valid for a drawing view that was previously made a Break View; in the FeatureManager design tree, *break\_view* **RMB menu > Break View** |
| **swCommands\_BreakCornerCornerTrim** | 364; valid for sheet metal parts; **Sheet Metal toolbar > Corners > Break-Corner/Corner-Trim** |
| **swCommands\_BrokenOutSection** | 328; valid for drawings; **Drawing toolbar > Broken-out Section** |
| **swCommands\_Browse** | 795; dialog resource **Browse** |
| **swCommands\_Build\_Doctor** | 1743; valid when a selected feature, component, or mate group has errors; **Tools menu > Evaluate > MateXpert** |
| **swCommands\_Bullet** | 533; valid for selected text; **Formatting toolbar > Bullet** |
| **swCommands\_CameraView** | 127; valid for models with cameras; **View toolbar > Camera View** |
| **swCommands\_Cancel** | 767; dialog resource button "Cancel" |
| **swCommands\_Cancel\_Command** | 3043; **Standard toolbar > Cancel** |
| **swCommands\_Cancel\_Edit\_Cntr** | 849; virtual key Esc |
| **swCommands\_Cancel\_Edit\_Srvr** | 850; virtual key Esc |
| **swCommands\_Capture\_3dView** | 3141; **SOLIDWORKS MBD toolbar > Capture 3D View** |
| **swCommands\_Capture\_RenderSystem\_ProfilingData** | 3359; only valid on the DebugDotMenu in SOLIDWORKS debug builds; **DotMenu > Display > Capture RenderSystem Profiling data** |
| **swCommands\_Caterpillar** | 516; valid for drawings; **Annotations toolbar > Caterpillar** |
| **swCommands\_Cavity** | 93; for assemblies with a mold base and design parts; **Mold Tools toolbar > Cavity** |
| **swCommands\_Cd\_Delete** | 689; dialog resource **Delete** |
| **swCommands\_Cd\_Deleteall** | 691; dialog resource **Delete All** |
| **swCommands\_Cd\_Edit** | 716; Relations dialog **Edit** |
| **swCommands\_Cd\_Undo** | 706; dialog resource **Undo** |
| **swCommands\_Center** | 390; valid for selected text; **Formatting toolbar > Center** |
| **swCommands\_Centerline** | 49; valid for parts with a selected sketch; **Sketch toolbar > Centerline** |
| **swCommands\_CenterMark** | 95; valid only for drawings; **Annotation toolbar > Center Mark** |
| **swCommands\_CenterpointArc** | 44; valid for parts and drawings; **Layout Tools toolbar > Arcs > Centerpoint Arc** or **Sketch toolbar > Arcs > Centerpoint Arc** |
| **swCommands\_CenterPointSnap** | 530; valid for sketches; **Quick Snaps toolbar > Center Point Snap** |
| **swCommands\_CentreRectangle** | 2794; valid for parts with a selected sketch; **Layout Tools toolbar > Rectangles > Center Rectangle** or **Sketch toolbar > Rectangles > Center Rectangle** |
| **swCommands\_CentreRectangleAtAngle** | 2795; valid for parts with a selected sketch; **Layout Tools toolbar > Rectangles >3 Point Center Rectangle** or **Sketch toolbar > Rectangles > 3 Point Center Rectangle** |
| **swCommands\_Chamfer** | 11; valid for parts; **Features toolbar > Chamfer** |
| **swCommands\_ChamferDimension** | 366; valid only for drawings; **Dimensions/Relations toolbar > Chamfer Dimension** |
| **swCommands\_Change\_DrView\_Reference** | 3094; valid only for drawings; **Drawing toolbar > Replace Model** |
| **swCommands\_Change\_Route\_Dia** | 2288; valid for the SOLIDWORKS Routing add-in and an open piping or flexible tubing assembly; **Routing Tools toolbar > Change Route Diameter** |
| **swCommands\_Change\_Write\_Access** | 2120; valid for models in a multi-user environment (select **Tools > Options > System Options > Collaboration > Add shortcut menu items for multi-user environment**; **File menu > Get Write Access** |
| **swCommands\_Change\_Write\_Access\_Comp** | 2119; valid for shared assemblies in a multi-user environment (select **Tools > Options > System Options > Collaboration > Add shortcut menu items for multi-user environment**; in the FeatureManager design tree, *comp* **RMB menu > Make Read-Only** or **Get Write Access** |
| **swCommands\_ChangeDisplayState** | 2926; valid for parts and assemblies; **View > Change Display States** |
| **swCommands\_ChangeLayer** | 3056; valid for drawings; **Line Format toolbar > Change Layer** |
| **swCommands\_ChangeSuppressionState** | 150; valid for assemblies with a selected component; **Assembly toolbar > Change Suppression State** |
| **swCommands\_ChangeTransparency** | 120; valid for assemblies with a selected component; **Assembly toolbar > Change Transparency** |
| **swCommands\_Check** | 133; **Tools toolbar > Check** |
| **swCommands\_Check\_Sketch\_For\_Feature** | 1138; valid for a part and an open sketch, opens the Check Sketch For Feature Usage dialog; **Tools menu > Sketch Tools > Check Sketch for Feature** |
| **swCommands\_CheckReadOnlyFiles** | 541; valid only if **Tools menu > Options > System Options > Collaboration > Enable Multi-user environment** and **Check if files opened read-only have been modified by other users** are both checked; **Standard > Check Read-only Files** |
| **swCommands\_Circle** | 46; for drawings, **Layout Tools toolbar > Circle**; for parts with a selected sketch or assemblies with a selected planar face, **Sketch toolbar > Circle** |
| **swCommands\_CircuitWorks** | 2893; **SOLIDWORKS Add-ins toolbar > CircuitWorks** |
| **swCommands\_CircularPattern** | 73; valid for parts; **Features toolbar > Circular Pattern** |
| **swCommands\_CircularSketchPattern** | 173; valid for parts with a sketch in edit mode; **Sketch toolbar > Circular Sketch Pattern** |
| **swCommands\_Clear\_List\_Box** | 1734; valid in list boxes in dialogs and PropertyManager pages; *list\_box* **RMB menu > Clear Selections** |
| **swCommands\_ClearAllFilters** | 274; **Selection Filter toolbar > Clear All Filters** |
| **swCommands\_ClearanceVerification** | 2848; valid for assemblies; **Assembly toolbar > Clearance Verification** |
| **swCommands\_ClickHereToSeeThePreview** | 5; alternative to swCommands\_Toolbar\_Inference; **View menu > Toolbars > Quick Snaps** |
| **swCommands\_ClosedCorner** | 360; valid for sheet metal parts; **Sheet Metal toolbar > Corners > Closed Corner** |
| **swCommands\_Cmark\_Merge** | 1893; valid for a drawing with two multi-selected center marks that are mergeable in the center mark set; in the graphics area, *center\_mark* **RMB menu > Merge Center Mark** |
| **swCommands\_Cmark\_Select** | 1898; valid for a drawing with a selected center mark in a center mark set; in the graphics area, *center\_mark* **RMB menu > Select Center Mark Set** |
| **swCommands\_Cmark\_Setbase** | 1873; valid for a drawing with a selected center mark in a center mark set; in the graphics area, *center\_mark* **RMB menu > Set as Base Center** |
| **swCommands\_Collapse\_Tree** | 1977; accelerator key ctrl-C |
| **swCommands\_Collapseallitems\_Tree** | 2555; accelerator key shift-C |
| **swCommands\_Color** | 531; valid for selected text; **Formatting toolbar > Color** |
| **swCommands\_ColorDisplayMode** | 299; **Line Format toolbar > Color Display Mode** |
| **swCommands\_Combine** | 407; valid for parts with two or more solid bodies; **Features >** **Combine** |
| **swCommands\_Command\_Option\_Toggle** | 1635; valid during insertion of a line in an open sketch; in the graphics area, *sketch\_line* **RMB menu > Switch to arc (A)** |
| **swCommands\_Comp\_Config\_Prop** | 941; valid for assemblies; in the FeatureManager design tree, *selected\_component* **RMB menu toolbar > Component Properties** |
| **swCommands\_Comp\_Display\_Hiddengreyed** | 2563; valid for assemblies; in the FeatureManager design tree, *selected\_component* **RMB menu > Component Display > Hidden Lines Visible** |
| **swCommands\_Comp\_Display\_Hiddengreyed\_All** | 2706; valid for a selected top-level-assembly; **Edit menu > Component Display > Hidden Lines Visible > All Display States** |
| **swCommands\_Comp\_Display\_Hiddengreyed\_Specify** | 2712; valid for a selected top-level-assembly, opens the Apply to Display States dialog; **Edit menu > Component Display > Hidden Lines Visible > Specified Display States** |
| **swCommands\_Comp\_Display\_Hiddenremoved** | 2564; valid for assemblies; in the FeatureManager design tree, *selected\_component* **RMB menu > Component Display > Hidden Lines Removed** |
| **swCommands\_Comp\_Display\_Hiddenremoved\_All** | 2707; valid for a selected top-level-assembly; **Edit menu > Component Display > Hidden Lines Removed > All Display States** |
| **swCommands\_Comp\_Display\_Hiddenremoved\_Specify** | 2713; valid for a selected top-level-assembly; **Edit menu > Component Display > Hidden Lines Removed > Specified Display States** |
| **swCommands\_Comp\_Display\_Shaded** | 2566; valid for assemblies; in FeatureManager design tree, *selected\_component* **RMB menu > Component Display > Shaded** |
| **swCommands\_Comp\_Display\_Shaded\_All** | 2709; valid for a selected top-level-assembly; **Edit menu > Component Display > Shaded > All Display States** |
| **swCommands\_Comp\_Display\_Shaded\_Specify** | 2715; valid for a selected top-level-assembly; **Edit menu > Component Display > Shaded > Specified Display States** |
| **swCommands\_Comp\_Display\_Shaded\_With\_Edges** | 2565; valid for assemblies; in FeatureManager design tree, *selected\_component* **RMB menu > Component Display > Shaded With Edges** |
| **swCommands\_Comp\_Display\_Shaded\_With\_Edges\_All** | 2708; valid for a selected top-level-assembly; **Edit menu > Component Display > Shaded With Edges > All Display States** |
| **swCommands\_Comp\_Display\_Shaded\_With\_Edges\_Specify** | 2714; valid for a selected top-level-assembly; **Edit menu > Component Display > Shaded With Edges > Specified Display States** |
| **swCommands\_Comp\_Display\_View\_Default** | 2567; valid for assemblies; in FeatureManager design tree, *selected\_component* **RMB menu > Component Display > Default Display** |
| **swCommands\_Comp\_Display\_View\_Default\_All** | 2710; valid for a selected top-level-assembly; **Edit menu > Component Display > Default Display > All Display States** |
| **swCommands\_Comp\_Display\_View\_Default\_Specify** | 2716; valid for a selected top-level-assembly; **Edit menu > Component Display > Default Display > Specified Display States** |
| **swCommands\_Comp\_Display\_Wireframe** | 2562; valid for assemblies; in FeatureManager design tree, *selected\_component* **RMB menu > Component Display > Wireframe** |
| **swCommands\_Comp\_Display\_Wireframe\_All** | 2705; valid for a selected top-level-assembly; **Edit menu > Component Display > Wireframe > All Display States** |
| **swCommands\_Comp\_Display\_Wireframe\_Specify** | 2711; valid for a selected top-level-assembly; **Edit menu > Component Display > Wireframe > Specified Display States** |
| **swCommands\_Comp\_Isolate** | 2726; valid for assemblies; in the FeatureManager design tree, *selected\_component* **RMB menu > Isolate** |
| **swCommands\_Comp\_Isolate\_Exit** | 2732; Isolate dialog **Exit** |
| **swCommands\_Comp\_Parent\_Child\_Rel** | 2627; valid for assemblies and drawings; in the FeatureManager design tree, *selected\_component* **RMB menu > Parent/Child** |
| **swCommands\_Component\_Color** | 653; alternative to swCommands\_EditColor, valid for a selected component in an assembly, opens the Sketch/Curve Color PropertyManager page; **Edit menu > Appearance > Sketch/Curve Color** |
| **swCommands\_Component\_Display** | 2561; in the FeatureManager design tree, *component\_name* **RMB menu > Component Display submenu** |
| **swCommands\_Component\_Pattern** | 1016; **Insert menu > Component Pattern submenu** |
| **swCommands\_Component\_Pattern\_Chain** | 3126; valid for assemblies; **Assembly toolbar > Chain Component Pattern** |
| **swCommands\_Component\_Pattern\_Circular** | 1942; valid for assemblies; **Assembly toolbar > Circular Component Pattern** |
| **swCommands\_Component\_Pattern\_Curve** | 3109; valid for assemblies; **Assembly toolbar > Curve Driven Component Pattern** |
| **swCommands\_Component\_Pattern\_Feature** | 1943; valid for assemblies; **Assembly toolbar > Pattern Driven Component Pattern** |
| **swCommands\_Component\_Pattern\_Linear** | 1941; valid for assemblies; **Assembly toolbar > Linear Component Pattern** |
| **swCommands\_Component\_Pattern\_Sketch** | 3108; valid for assemblies; **Assembly toolbar > Sketch Driven Component Pattern** |
| **swCommands\_Component\_Properties** | 864; valid for drawings, opens the Component Line Font dialog; in the FeatureManager design tree or drawing view, *selected\_component* **RMB menu > Component Line Font** |
| **swCommands\_Component\_Reload** | 1527; valid for assemblies; in the FeatureManager design tree, *selected\_component* **RMB menu > Reload** |
| **swCommands\_Component\_RV\_Appearance** | 2898; in the FeatureManager design tree, *component\_name* **RMB context toolbar > Appearances >** *component\_name* |
| **swCommands\_Component\_Texture** | 654; valid for a selected component in an assembly, opens the Texture PropertyManager page |
| **swCommands\_CompositeCurve** | 158; valid for parts; **Features toolbar > Curves > Composite Curve** or **Curves toolbar > Composite Curve** |
| **swCommands\_Conc\_Dim\_Show\_Extn\_Lines** | 1995; valid for drawings; *concentric\_dimension\_extension\_line* **RMB menu > Show extension lines** |
| **swCommands\_ConfigurationsToolbar** | 3117; **View menu > Toolbars > Configurations** |
| **swCommands\_Conic** | 3049; valid for parts with a selected sketch; **Sketch toolbar > Conic** |
| **swCommands\_ConstructionGeometry** | 102; valid for parts with an open sketch and selected sketch entity; **Sketch toolbar > Construction Geometry** |
| **swCommands\_Convert\_To\_Bom98** | 1585; valid for a selected OLE item in a drawing view; in the graphics area, *dr\_view\_OLE\_item* **RMB menu > Convert to SOLIDWORKS 98 and later Format** |
| **swCommands\_ConvertEntities** | 57; valid for parts with an open sketch; **Sketch toolbar > Convert Entities** |
| **swCommands\_ConvertMeshBody2Classic** | 3531; converts recognized mesh brep faces to standard BREP faces; **Insert >** **Features > Convert Mesh to Standard...** |
| **swCommands\_ConvertMeshSolidSurface** | 3245; converts a selected solid or surface body to a Parasolid mesh body; **Feature toolbar > ConvertMesh Bodies...** |
| **swCommands\_ConvertTo\_Base\_Dimension** | 3408; valid for a selected dimension in a chain dimension set, replaces all dimensions in the set with baseline dimensions; **RMB menu > Convert To Base** |
| **swCommands\_ConvertTo\_Chain\_Dimension** | 3407; valid for a selected dimension in a baseline dimension set, replaces all dimensions in the set with chain dimensions; **RMB menu > Convert To Chain** |
| **swCommands\_ConvertToGeneric** | 3364; converts the selected interpolating spline into a generic spline; **Tools > Spline Tools > Convert to Generic Spline...** |
| **swCommands\_ConvertToModif** | 3124; valid for open sketches of a selected style spline; **Spline Tools toolbar > Convert to Spline** |
| **swCommands\_ConvertToStyle** | 3123; valid for open sketches of a selected interpolating spline; **Spline Tools toolbar > Convert to Style Spline** |
| **swCommands\_CoordinateSystem** | 154; valid for parts with a selected sketch; **Features toolbar > Reference Geometry > Coordinate System** |
| **swCommands\_Copy** | 583; valid for a selection; **Standard >**  **Copy** |
| **swCommands\_Copy\_Appearance** | 3053; valid for a model with an appearance; **Render Tools** or **View toolbar > Copy Appearance** |
| **swCommands\_Copy\_Bookmark\_Link** | 3526; valid only in SOLIDWORKS Connected, copies the link of the bookmarked file location in bookmarks to the clipboard; **Lifecycle and Collaboration toolbar > Bookmarks > Copy Bookmark Link** |
| **swCommands\_Copy\_Drw\_To\_Dwgeditor** | 2202; valid for drawings; **Edit menu > Copy to DWG format** |
| **swCommands\_Copy\_Swift\_Schema** | 2017; valid for parts with multiple configurations and a selected configuration to which to copy an existing tolerance scheme; **DimXpert toolbar > Copy Scheme** |
| **swCommands\_CopyEntities** | 559; vald for parts with a sketch in edit mode; **Sketch toolbar > Copy Entities** |
| **swCommands\_Core** | 514; valid for parts with a selected plane or planar face; **Mold Tools toolbar > Core** |
| **swCommands\_Corner\_Relief** | 3112; valid for sheet metal parts and multiple selected faces that define corners; **Sheet Metal toolbar > Corner Relief** |
| **swCommands\_CosmeticThread** | 115; valid for parts with a selected circular edge; **Annotation > Cosmetic Thread** |
| **swCommands\_CosmeticWeld** | 2991; valid for parts or assemblies with a selected assembly feature, opens the Weld Bead PropertyManager page; **Weldments toolbar** or **Insert menu > Assembly Features > Weld Bead** |
| **swCommands\_COSMOSFloXpress** | 2834; **Tools toolbar > FloXpress Analysis Wizard** |
| **swCommands\_CosmosMotion** | 621; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Motion** |
| **swCommands\_CosmosworksDesigner** | 565; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Simulation** |
| **swCommands\_CosmosxpressAnalysisWizard** | 439; **Tools toolbar > SimulationXpress Analysis Wizard** |
| **swCommands\_Create\_Cut\_List\_Folder** | 2512; valid for weldment parts; in the FeatureManager design tree, *solid\_body* **RMB menu > Create Cut List Item** |
| **swCommands\_Create\_Empty\_Folder** | 1906; in the FeatureManager design tree, *item\_name* **RMB menu > Create New Folder** |
| **swCommands\_Create\_New\_Configuration** | 2022; in the FeatureManager design tree, *component\_name* **RMB menu > Add Configuration** |
| **swCommands\_Create\_Sub\_Bodyfolder** | 2570; in the FeatureManager design tree, *solid\_body\_name* **RMB menu > Add to New Folder** |
| **swCommands\_Create\_Sub\_LiveSectionFolder** | 2884; valid for parts with a Live Section Plane; in the FeatureManager Design Tree, **Live Section Planes** **folder** **RMB menu > Add to New Folder** |
| **swCommands\_Create\_Sub\_Weldment** | 2367; valid for weldment parts; in the FeatureManager design tree, **Cutlist folder >** *item\_name* **RMB menu > Create Sub-Weldment** |
| **swCommands\_Create\_Userdefined\_Rt\_By\_Drag\_Drop** | 3163; valid for the SOLIDWORKS Routing add-in and a routing assembly; **User Defined Route toolbar > Start by Drag/Drop** |
| **swCommands\_Create\_Userdefined\_Rt\_On\_Fly** | 3166; valid for the SOLIDWORKS Routing add-in and a routing assembly, opens the Connection Point PropertyManager page; **User Defined Route toolbar > Start at Point** |
| **swCommands\_CreateSketchFromSelections** | 381; valid for parts, creates a new sketch from selected sketch entities; **2D To 3D** **toolbar > Create Sketch from Selections** |
| **swCommands\_CropView** | 311; valid for drawings with a closed sketch profile on a selected view; **Drawing toolbar > Crop View** |
| **swCommands\_Cull\_Dynamic\_Update** | 1799; valid for assemblies; **View menu > Display > Optimize Zoom/Pan/Rotate** |
| **swCommands\_Curvature** | 132; **View toolbar > Curvature** |
| **swCommands\_CurvatureHedgehog** | 3130; **View toolbar > Surface Curvature** **Combs** |
| **swCommands\_CurveDrivenPattern** | 362; valid for parts with a selected sketch; **Features toolbar > Curve Driven Pattern** |
| **swCommands\_Curves** | 477; alternative to swCommands\_Toolbar\_Curve; **View menu > Toolbars > Curves** |
| **swCommands\_CurveThroughReferencePoints** | 123; valid for parts with a selected sketch; **Features toolbar > Curves > Curve Through Reference Points** |
| **swCommands\_CurveThroughXYZPoints** | 128; valid for parts with a selected sketch; **Features toolbar > Curves > Curve Through XYZ Points** |
| **swCommands\_Custom\_Msg\_Display\_Camera\_By\_Name** | 2239; alternative to swCommands\_Anim\_Custom\_Msg\_Display\_Camera\_By\_Name; valid only in context of Motion Study gantt chart pop-up menus; In Motion Study gantt chart, *orientation\_and\_camera\_views\_time\_bar\_key* **RMB menu > View Orientation >***camera\_view\_name* |
| **swCommands\_Custom\_Msg\_Display\_Vw\_By\_Name** | 2238; menu item valid only in context of view orientations |
| **swCommands\_Customization\_And\_More** | 1938; **File menu > Customize Menu** and many **RMB menu > Customize menu** |
| **swCommands\_Cut** | 584; **Standard toolbar > Cut** |
| **swCommands\_CutListSortingOptions** | 3431; valid for a model with cut list items, opens the Cut List Sorting Options PropertyManager for the selected cut list folder; **FeatureManager design tree cut list folder RMB menu > Cut List Sorting Options** |
| **swCommands\_CutWithSurface** | 101; **Features toolbar > Cut With Surface** |
| **swCommands\_CVSpline** | 3099; **Sketch toolbar > Style Spline** |
| **swCommands\_DatumFeature** | 114; **Annotation toolbar > Datum Feature** |
| **swCommands\_DatumTarget** | 122; **Annotation toolbar > Datum Feature** |
| **swCommands\_DecimateMesh** | 3429; simplifies facet counts for graphics and mesh BRP bodies; **Features toolbar > Decimate Mesh Body** |
| **swCommands\_DecreaseIndent** | 543; valid for selected text; **Formatting toolbar > Decrease indent** |
| **swCommands\_Defeature** | 3050; valid for parts or assembles with a selected Defeature item; **RMB menu > Update Defeature** |
| **swCommands\_Defer** | 708; dialog resource **Show preview** |
| **swCommands\_DefineStructConnection** | 3415; **Structure System toolbar > Define Connection Element** |
| **swCommands\_Deform** | 454; valid for parts; **Features toolbar > Deform** |
| **swCommands\_Deform\_Rmb\_Add\_Connector** | 754; valid when the Deform or Loft PropertyManager page is open, the Deform Type is Curve to curve, and an entity is selected; in the graphics area, *entity* **RMB menu > Add Connector** |
| **swCommands\_Deform\_Rmb\_Delete\_All\_Connector** | 2610; valid when the Loft PropertyManager page is open; in the graphics area, **RMB menu > Delete all connectors** |
| **swCommands\_Deform\_Rmb\_Delete\_Connector** | 2609; valid when the Deform or Loft PropertyManager page is open, and a connector is selected; in the graphics area, *connector* **RMB menu > Delete Connector** |
| **swCommands\_Deform\_Rmb\_Disp\_Connectionlines** | 756; valid when the Deform PropertyManager page is open, and Deform Type is Curve to curve; in the graphics area, **RMB menu > Show Connection Lines** |
| **swCommands\_Deform\_Rmb\_Set\_Transparent** | 751; valid when the Deform PropertyManager page is open; in the graphics area, **RMB menu > Transparent Preview** |
| **swCommands\_Deform\_Rmb\_Set\_Zebra** | 752; valid when the Deform PropertyManager page is open; in the graphics area, **RMB menu > Zebra Stripes Preview** |
| **swCommands\_Deform\_Rmb\_Show\_Connector** | 2608; valid when the Deform or Loft PropertyManager page is open, and a connector has been hidden; in the graphics area, *connector* **RMB menu > Show Connector** |
| **swCommands\_Deform\_Rmb\_Update\_Display** | 755; valid when the Deform PropertyManager page is open; in the graphics area, **RMB menu > Show Preview** |
| **swCommands\_Del\_Equation** | 1580; valid in the Equations, Global Vairables, and Dimensions dialog; *row* **RMB menu > Delete Equation** |
| **swCommands\_Delete** | 16; deletes a selected item; **Standard toolbar > Delete** |
| **swCommands\_Delete\_All\_Constraints** | 1763; valid only in specific dialogs involving sketch constraints, such as the Display/Delete Relations PropertyManager page; *relations\_list\_box* **RMB menu > Delete All** |
| **swCommands\_Delete\_Annotation\_View** | 2215; valid for drawing annotation views; *annotation\_view* **RMB menu > Delete** |
| **swCommands\_Delete\_Comment** | 2070; in the FeatureManager design tree, *comment\_name* **RMB menu > Delete Comment** |
| **swCommands\_Delete\_Constraints** | 709; Move Confirmation or Copy Confirmation dialog resource **Delete** |
| **swCommands\_Delete\_Cut\_List** | 2640; in the FeatureManager design tree, *cut\_list\_folder* **RMB menu > Delete** |
| **swCommands\_Delete\_List\_Box\_Item** | 1735; valid in dialog list boxes; **RMB > Delete** |
| **swCommands\_Delete\_Pgm\_Sketch\_Offset** | 2434; valid for an open sketch with one or more offset entities; *sketch\_offset\_line* **RMB menu > Delete Offset** |
| **swCommands\_Delete\_Relation** | 679; Equations dialog resource **Delete** |
| **swCommands\_Delete\_Selected\_Constraint** | 1809; valid in specific dialogs involving sketch constraints, such as Display/Delete Relations PropertyManager page; *relations\_list\_box* **RMB menu > Delete** |
| **swCommands\_Delete\_Smart\_Fastener** | 2457; valid only for Toolbox add-ins and assemblies and only when editing a Smart Fastener grouping; in the Smart Fasteners PropertyManager page,  **Results > Group1 > Series1** **RMB menu > Delete** |
| **swCommands\_Delete\_Weldment** | 2361; valid only for weldments; in the FeatureManager design tree, *weldment\_name* **RMB menu > Delete** |
| **swCommands\_DeleteFace** | 393; **Surfaces toolbar > Delete Face** |
| **swCommands\_DeleteHoleSurface** | 3360; deletes inner cavity on surfaces; **Surfaces toolbar > Delete Hole** |
| **swCommands\_DeleteSolidSurface** | 424; **Feaures toolbar > Delete/Keep Body** |
| **swCommands\_Derive\_Sketch** | 1009; valid for a multi-selected sketch and a face or a plane; **Insert menu > Derived Sketch** |
| **swCommands\_Design\_Study** | 2953; **Tools toolbar > Design Study** |
| **swCommands\_DesignChecker** | 460;  **SOLIDWORKS Add-ins toolbar > Design Checker** |
| **swCommands\_DesignStudy\_Add\_Parameters** | 2955; valid for parts, opens the Parameters dialog; **Insert menu > Design Study > Parameters** |
| **swCommands\_DesignTable** | 413; **Tools toolbar > Design Table** |
| **swCommands\_DetailView** | 35; valid for drawings; **Drawing toolbar > Detail View** |
| **swCommands\_DeviationAnalysis** | 411; valid for parts; **Tools toolbar > Deviation Analysis** |
| **swCommands\_DFMXpress** | 2833; valid for parts; **Tools toolbar > DFMXpress Analysis Wizard** |
| **swCommands\_Dim\_Center\_Text** | 1574; centers a selected dimension between extension lines; in the graphics area, *dimension* **RMB menu > Display Options > Center Dimension** |
| **swCommands\_Dim\_Foreshort** | 2645; valid for a selected dimension; in the graphics area, *dimension* **RMB menu > Display Options > Foreshorten** |
| **swCommands\_Dim\_Inspection** | 1342; valid for a selected dimension; in the graphics area, *dimension* **RMB menu > Display Options > Show as Inspection** |
| **swCommands\_Dim\_Jog** | 2839; valid for a selected dimension; in the graphics area, *dimension\_extension\_line* **RMB menu > Display Options > Jog** |
| **swCommands\_Dim\_RadialDiametric\_Toggle** | 3470; Toggles display dimension from single distance to doubled distance and vice versa |
| **swCommands\_Dim\_Restore\_Original\_Value** | 3522; valid for a selected overridden dimension; in the graphics area, *overridden\_dimension* **RMB menu > Dimension > Restore Original Value** |
| **swCommands\_Dim\_Showpara** | 1572; valid for a selected dimension; in the graphics area, *dimension* **RMB menu > Display Options > Show Parentheses** |
| **swCommands\_Dim\_Snap\_Horizontal** | 787; valid for a selected vertical dimension; in the graphics area, *vertical\_dimension* **RMB menu > Set Horizontal** |
| **swCommands\_Dim\_Snap\_To\_Edge** | 789; valid for a selected horizontal dimension; in the graphics area, *horizontal\_dimension* **RMB menu > Align to edge** |
| **swCommands\_Dim\_Snap\_Vertical** | 788; valid for a selected horizontal dimension; in the graphics area, *horizontal\_dimension* **RMB menu > Set Vertical** |
| **swCommands\_Dim\_Stop\_Break** | 2785; valid for a selected dimension; in the graphics area, *dimension\_with\_break\_lines* **RMB menu > Remove Dimension Breaks** |
| **swCommands\_Dimension\_Driven\_Toggle** | 3025; valid for an open sketch with an active sketch tool; **Sketch toolbar > Sketch Dimension Driven** |
| **swCommands\_DimensionAlignCollinear** | 2974; valid for multi-selected dimensions; **Align toolbar > Align Collinear** |
| **swCommands\_DimensionPattern** | 3101; valid for parts with a selected sketch; **Features toolbar > Dimension Pattern** |
| **swCommands\_DimensionRelations** | 490; alternative to swCommands\_Toolbar\_Sketch\_Rels; **View menu > Toolbars > Dimensions/Relations** |
| **swCommands\_DimensionSpaceEvenly** | 2973; valid for multi-selected dimensions; **Align toolbar > Dimension Space Evenly/Radial** |
| **swCommands\_DimensionStagger** | 2975; valid for multi-selected dimensions; **Align toolbar > Align Stagger** |
| **swCommands\_DimensionTextAlignBottom** | 2978; valid for multi-selected dimensions; **Align toolbar > Bottom Justify Dimension Text** |
| **swCommands\_DimensionTextAlignLeft** | 2979; valid for multi-selected dimensions; **Align toolbar > Left Justify Dimension Text** |
| **swCommands\_DimensionTextAlignRight** | 2980; valid for multi-selected dimensions; **Align toolbar > Right Justify Dimension Text** |
| **swCommands\_DimensionTextAlignTop** | 2977; valid for multi-selected dimensions; **Align toolbar > Top Justify Dimension Text** |
| **swCommands\_Dimetric** | 468; **View toolbar > View Orientation > Dimetric** |
| **swCommands\_Disp\_Dim\_As\_Diameter** | 3486; Left or right click circular entity, display dimension context toolbar > diameter button |
| **swCommands\_Disp\_Dim\_As\_Linear** | 3487; Left or right click circular entity, display dimension context toolbar > linear diameter button |
| **swCommands\_Disp\_Dim\_As\_Radius** | 3485; Left or right click circular entity, display dimension context toolbar > radius button |
| **swCommands\_Display\_States\_Target** | 3195; opens the Display State Target dialog; **Render Tools toolbar > Display States Target** |
| **swCommands\_DisplayControlPolygon** | 572; valid for a selected sketch spline; **Spline Tools toolbar > Display Control Polygon** |
| **swCommands\_DisplayDeleteRelations** | 60; valid for drawings; **Layout toolbar > Display/Delete Relations** |
| **swCommands\_Dissolve\_Lib\_Feature** | 1576; valid for parts with a library feature; in the FeatureManager design tree, *library\_feature* **RMB menu > Dissolve Library Feature** |
| **swCommands\_Dissolve\_Sktext** | 2470; valid for an open sketch with sketch text; in the graphics area, *sketch\_text* **RMB menu > Dissolve Sketch Text** |
| **swCommands\_Dissolve\_Subassembly** | 1260; valid for assemblies with subassemblies; in the FeatureManager design tree, *subassembly\_name* **RMB menu > Dissolve Subassembly** |
| **swCommands\_DissolveEntities** | 3306; dissolves selected autoexplode lines so they can be edited as regular entities; **Sketch toolbar > Dissolve Entities** |
| **swCommands\_DocumentFont** | 387; valid for annotations with text; **Formatting toolbar > Document Font** |
| **swCommands\_Dome** | 137; valid for parts with a selected face; **Features toolbar > Dome** |
| **swCommands\_DowelPinSymbol** | 369; valid for drawings with circular edges or arcs; **Annotation toolbar > Dowel Pin Symbol** |
| **swCommands\_DraftQualityHlrHlv** | 298; **View toolbar > Draft Quality HLR/HLV** |
| **swCommands\_Draw\_Bl\_Isozag** | 1582; valid for a drawing when the Broken View PropertyManager page is open; in the graphics area, *break\_line* **RMB menu >** **Small Zig Zag Cut** |
| **swCommands\_Draw\_Bl\_Spline** | 1522; valid for a drawing when the Broken View PropertyManager page is open; in the graphics area, *break\_line* **RMB menu >****Curve Cut** |
| **swCommands\_Draw\_Bl\_Straight** | 1521; valid for a drawing when the Broken View PropertyManager page is open; in the graphics area, *break\_line* **RMB menu >** **Straight Cut** |
| **swCommands\_Draw\_Bl\_Zigzag** | 1523; valid for a drawing when the Broken View PropertyManager page is open; in the graphics area, *break\_line* **RMB menu >** **Zig Zag Cut** |
| **swCommands\_Drawing\_Feat\_Edit** | 2693; valid for drawing views; in the FeatureManager design tree, *sheet***>** *drawing\_view* **RMB menu > Edit Feature** |
| **swCommands\_Drawing\_Feat\_Edit\_Def** | 2497; in the FeatureManager design tree, *macro\_feature* **RMB menu > Edit Definition** |
| **swCommands\_Drawing\_Stats** | 2172; valid for drawings; **Tools menu > Evaluate > Performance Evaluation** |
| **swCommands\_Drawings** | 478; alternative to swCommands\_Toolbar\_Drawing; **View menu > Toolbars > Drawing** |
| **swCommands\_Driven\_Dim** | 1908; valid for a selected drawing dimension; in the graphics area, *dim* **RMB menu > Driven** |
| **swCommands\_DriveWorkXxpress** | 2832; **Tools toolbar > DriveWorksXpress Wizard** |
| **swCommands\_Drview\_Load\_Model** | 649; valid for detached drawings; *drawing\_view* **RMB menu > Load Model** |
| **swCommands\_Drw\_Rebuild\_All** | 1796; valid for drawings with a modified part when **Automatic view update** is not set in the FeatureManager design tree, *top-level\_drawing* **RMB menu > Update All Views** |
| **swCommands\_Dt\_Save\_Table** | 2508; valid for models with design tables; in the ConfigurationManager, **Tables folder > Design Table RMB menu > Save Table** |
| **swCommands\_Dv\_Suppress** | 1503; valid for a selected drawing view that is unsuppressed; in the graphics area, *dr\_view* **RMB menu > Hide** |
| **swCommands\_Dv\_Unsuppress** | 1504; valid for a selected drawing view that is suppressed; in the graphics area, *dr\_view* **RMB menu > Show** |
| **swCommands\_Dve\_Blind** | 1447; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, **RMB menu > Direction 1 > Blind** |
| **swCommands\_Dve\_Mid\_Plane** | 1446; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, **RMB menu > Direction 1 > Mid Plane** |
| **swCommands\_Dve\_Offsetfromsurface** | 1450; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, **RMB menu > Direction 1 > Offset From Surface** |
| **swCommands\_Dve\_Rmb\_Back** | 2164; valid for some open PropertyManager pages; in the graphics area, **RMB menu > Back** |
| **swCommands\_Dve\_Rmb\_Cancel** | 1465; valid when a PropertyManager page is open; in the graphics area, **RMB menu > Cancel** |
| **swCommands\_Dve\_Rmb\_Close\_Spline\_Curve** | 1653; valid when the Curve Through Reference Point PropertyManager page is open; in the graphics area, **RMB menu > Closed Curve** |
| **swCommands\_Dve\_Rmb\_Exit\_Preview** | 2439; valid when the Detailed Preview PropertyManager page is open; in the graphics area, **RMB menu > Exit Preview** |
| **swCommands\_Dve\_Rmb\_Lpat\_Flip\_Direction1** | 1657; valid when the LPattern1 PropertyManager page is open; in the graphics area, **RMB menu > Reverse Direction 1** |
| **swCommands\_Dve\_Rmb\_Lpat\_Flip\_Direction2** | 1658; valid when the LPattern1 PropertyManager page is open; in the graphics area, **RMB menu > Reverse Direction 2** |
| **swCommands\_Dve\_Rmb\_Lpat\_Geometry\_Pattern** | 1656; valid when the LPattern1 PropertyManager page is open; in the graphics area, **RMB menu > Geometry Pattern** |
| **swCommands\_Dve\_Rmb\_Lpat\_Varysketch** | 1655; valid when the LPattern1 PropertyManager page is open for a model with a driving dimension selected for Pattern Direction 1; in the graphics area, **RMB menu > Vary sketch** |
| **swCommands\_Dve\_Rmb\_Mc\_Select\_Entities** | 743; valid when the Move or Copy PropertyManager page is open; in the graphics area, **RMB menu > Select Entities** |
| **swCommands\_Dve\_Rmb\_Next** | 2165; valid for some open PropertyManager pages; in the graphics area, **RMB menu > Next** |
| **swCommands\_Dve\_Rmb\_Ok** | 1463; valid when a PropertyManager page is open; in the graphics area, **RMB menu > OK** |
| **swCommands\_Dve\_Rmb\_Pushpin** | 740; valid when the Planar Surface PropertyManager page is open; in the graphics area, **RMB menu > Pin Dialog** |
| **swCommands\_Dve\_Rmb\_Redo** | 1947; valid when a PropertyManager page is open, and **Redo** is enabled; in the graphics area, **RMB menu > Redo** |
| **swCommands\_Dve\_Rmb\_Select\_Feature** | 2459; valid when a PropertyManager page is open, and feature selection is enabled; in the graphics area, **RMB menu > Select Feature** |
| **swCommands\_Dve\_Rmb\_Undo** | 1945; valid when a PropertyManager page is open, and **Undo** is enabled; in the graphics area, **RMB menu > Undo** |
| **swCommands\_Dve\_Throughall** | 1451; valid when the Cut-Extrude PropertyManager page is open; in the graphics area, **RMB menu > Direction 1 > Through All** |
| **swCommands\_Dve\_ThroughAll\_Both** | 3092; valid when the Cut-Extrude PropertyManager page is open; in the graphics area, **RMB menu > Direction 1 > Through All - Both Directions** |
| **swCommands\_Dve\_Throughnext** | 1452; valid when the Cut-Extrude PropertyManager page is open; in the graphics area, **RMB menu > Direction 1 > Up To Next** |
| **swCommands\_Dve\_Uptobody** | 2509; valid when the Surface-Extrude PropertyManager page is open; in the graphics area, **RMB menu > Direction 1 > Up To Body** |
| **swCommands\_Dve\_Uptosurface** | 1449; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, **RMB menu > Direction 1 > Up To Surface** |
| **swCommands\_Dve\_Uptovertex** | 1448; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, **RMB menu > Direction 1 > Up To Vertex** |
| **swCommands\_Dymparam\_Dlg\_Cancel** | 1037; valid on a change parameter dialog pop-up toolbar |
| **swCommands\_Dymparam\_Dlg\_Designintent** | 1041; valid on a change parameter dialog pop-up toolbar |
| **swCommands\_Dymparam\_Dlg\_Increment** | 1040; valid on a change parameter dialog pop-up toolbar |
| **swCommands\_Dymparam\_Dlg\_Ok** | 1036; valid on a change parameter dialog pop-up toolbar |
| **swCommands\_Dymparam\_Dlg\_Regen** | 1039; valid on a change parameter dialog pop-up toolbar |
| **swCommands\_Dymparam\_Dlg\_Reverse** | 1038; valid on a change parameter dialog pop-up toolbar |
| **swCommands\_Dynamic\_Annotation\_Views** | 3145; **View (Heads-Up) toolbar > Dynamic Annotation Views** |
| **swCommands\_DynamicMirrorEntities** | 529; valid for parts with an open sketch and selected sketch segment about which to mirror; **Sketch toolbar > Dynamic Mirror Entities** |
| **swCommands\_EdgeFlange** | 359; valid for sheet metal parts; **Sheet Metal toolbar > Edge Flange** |
| **swCommands\_Edit\_Ang\_Ordinate** | 3082; valid for drawings of circles or arcs with angular running dimensions; in the graphics area, *angular\_running\_dimensi*on **RMB menu > Add to Running Dimension** |
| **swCommands\_Edit\_Annotation\_View** | 2234; in the FeatureManager design tree, **Annotations folder >** a*nnotation\_view* **RMB menu > Edit Annotation View** |
| **swCommands\_Edit\_Assembly** | 967; valid for assemblies with subassemblies; in the FeatureManager design tree, *subassembly\_name* **RMB minibar > Edit Assembly** or **Assembly toolbar > Edit Component** |
| **swCommands\_Edit\_Broken\_Out\_Section** | 1678; valid for a selected Broken-Out Section; in the FeatureManager design tree, *broken\_out\_section* **RMB menu > Edit Definition** |
| **swCommands\_Edit\_Cavity\_Part** | 1741; valid for a selected body feature used in mold creation; *sel\_body* **RMB menu > Edit Cavity Part** |
| **swCommands\_Edit\_Comment** | 2071; in the FeatureManager design tree, *comment\_name* **RMB menu > Edit Comment** |
| **swCommands\_Edit\_Csk\_Pattern** | 1392; valid for circular sketch patterns; in the graphics area, *circular\_sketch\_entity* **RMB menu > Edit Circular Pattern** |
| **swCommands\_Edit\_Cut\_List\_Folder\_Props** | 2513; valid for weldments with a cut list folder; in the FeatureManager design tree, *cut\_list\_item* **RMB menu > Properties** |
| **swCommands\_Edit\_Decal** | 2207; **Render Tools toolbar > Edit Decal** |
| **swCommands\_Edit\_Def\_Assy** | 655; valid for Smart Components open in edit mode; in the FeatureManager design tree, **Smart Feature folder > RMB menu > Edit in Defining Assembly** |
| **swCommands\_Edit\_Delete\_Replay** | 1907; valid for a selected animation feature; **RMB menu > Delete Replay** |
| **swCommands\_Edit\_Dissolve\_Assembly** | 1324; valid for a selected subassembly; **Edit menu > Dissolve Assembly** |
| **swCommands\_Edit\_Dragitem** | 831; valid for assemblies with MateReferences folders; in the FeatureManager design tree, **MateReferences folder >** *mate\_reference* **RMB menu > Edit Definition** |
| **swCommands\_Edit\_Drawview\_Sketch** | 1530; valid for drawing detail views or broken-out sections; **FeatureManager design tree >** *detail\_view* **folder >** *detail\_circle* **RMB menu > Edit Sketch** |
| **swCommands\_Edit\_Equation** | 1578; valid for a selected dimension with equations; *sel\_dim* **RMB menu > Edit Equation** |
| **swCommands\_Edit\_Exit\_No\_Save** | 1787; **Edit menu > Exit Sketch without Saving Changes** |
| **swCommands\_Edit\_Familytable** | 866; valid for models with design tables; **Edit menu > Design Table > Edit Table** or in ConfigurationManager, **Tables folder > Design Table RMB menu > Edit Table** |
| **swCommands\_Edit\_Familytable\_Open** | 867; valid for models with design tables; **Edit menu > Design Table > Edit Table in New Window** or in ConfigurationManager, **Tables folder > Design Table RMB menu > Edit Table in New Window** |
| **swCommands\_Edit\_Findinfm** | 1588; opens the Find In FeatureManager Design Tree dialog; in the FeatureManager design tree, *fm\_item* **RMB menu > Go To** |
| **swCommands\_Edit\_Flex\_Tube\_Rt** | 2260; valid for the SOLIDWORKS Routing add-in and an open flexible tube routing assembly; **Flexible Tubing toolbar > Edit Route** |
| **swCommands\_Edit\_Folder\_Feat** | 2390; valid for assemblies with a Mate group; **Mates folder RMB menu > Edit Features** |
| **swCommands\_Edit\_Importfolder** | 1583; valid for a selected import folder; *sel\_folder* **RMB menu > Edit import folder** |
| **swCommands\_Edit\_Incontext** | 868; edits the selected model in the context of the assembly where it was created; in the FeatureManager design tree, *model\_name* **RMB menu > Edit in Context** |
| **swCommands\_Edit\_Layout** | 2818; valid for assemblies; **Layout Tools toolbar > Layout** |
| **swCommands\_Edit\_Lsk\_Pattern** | 1391; valid for open sketches with linear sketch patterns; in the graphics area, *lin\_sketch\_pattern\_entity* **RMB menu > Edit Linear Pattern** |
| **swCommands\_Edit\_Ordinate** | 1507; valid for drawings with an ordinate dimension; in the graphics area, *ordinate\_dim* **RMB Menu > Add to Ordinate** |
| **swCommands\_Edit\_Paragraph** | 2068; valid for selected text; **Formatting toolbar > Paragraph Properties** |
| **swCommands\_Edit\_Part** | 965; valid for assemblies; in the FeatureManager design tree, *part\_name* **RMB context toolbar > Edit Part**; alternative to **Assembly toolbar > Edit Component** |
| **swCommands\_Edit\_Pipe\_Rt** | 2256; valid for the SOLIDWORKS Routing add-in and an open piping assembly; **Piping toolbar > Edit Route** |
| **swCommands\_Edit\_Polygon** | 1398; valid for an open sketch of a polygon; in the graphics area, *polygon\_entity* **RMB menu > Edit polygon** |
| **swCommands\_Edit\_Redolist** | 1456; valid for models with an undo list; **Standard toolbar > Redo** |
| **swCommands\_Edit\_Rollback** | 815; valid for a model rebuilt with a feature; in the FeatureManager design tree, *added\_feature* **RMB context toolbar > Rollback** or **Edit menu > Rollback** |
| **swCommands\_Edit\_Rolltoend** | 2503; valid for rolled back models; in the FeatureManager design tree, *rolled\_back\_feat\_name* **RMB menu > Roll to End** or **Edit menu > Roll to End** |
| **swCommands\_Edit\_Rolltoforward** | 2506; valid for a selected rolled back feature; in the FeatureManager design tree, *rolled\_back\_feat\_name* **RMB menu > Roll Forward** |
| **swCommands\_Edit\_Rolltoprevious** | 2502; valid for rolled back models; in the FeatureManager design tree, *rolled\_back\_feat\_name* **RMB menu > Roll to Previous** or **Edit menu > Roll to Previous** |
| **swCommands\_Edit\_Rtl\_Mode** | 2166; **Text editor popup menu > Right to left reading order** |
| **swCommands\_Edit\_RV\_Appearance** | 2821; **Render Tools** or **View toolbar > Edit Appearance** |
| **swCommands\_Edit\_Scene** | 2967; **Render Tools toolbar > Edit Scene** |
| **swCommands\_Edit\_Seed\_Feature** | 1242; valid for parts with a pattern feature; in the graphics area, *pattern\_entity* **RMB menu > Edit Seed Feature** |
| **swCommands\_Edit\_Select\_All** | 3027; **Standard toolbar > Select All** |
| **swCommands\_Edit\_Sheet** | 1502; finishes editing a drawing sheet in edit sheet format mode; in the FeatureManager design tree or the graphics area, *sheet* **RMB menu > Edit Sheet** |
| **swCommands\_Edit\_Sk\_Pattern** | 1816; valid for a selected non-polygonal pattern relation; *constraint* **RMB menu > Edit Pattern** |
| **swCommands\_Edit\_Sketch** | 859; valid for sketches; **Edit menu > Sketch** or in the FeatureManager design tree, *sketch\_name* **RMB context toolbar > Edit Sketch** |
| **swCommands\_Edit\_Sketch\_Belt** | 2750; valid for sketch belts; in the FeatureManager design tree, *belt\_name* **RMB menu > Edit Belt** |
| **swCommands\_Edit\_Sketchplane** | 863; valid for sketches; in the FeatureManager design tree or the graphics area, *sketch* **RMB context toolbar > Edit Sketch Plane** |
| **swCommands\_Edit\_Smart\_Comp\_Inst** | 2221; valid for assemblies with Smart Features; in the FeatureManager design tree, *smart\_feature* **RMB menu > Edit Feature** |
| **swCommands\_Edit\_Smart\_Fastener** | 2463; valid only for Toolbox add-ins and assemblies and existing Smart Fasteners; in the FeatureManager design tree, *smart\_fastener\_feature* **RMB menu > Edit Smart Fastener** |
| **swCommands\_Edit\_Smart\_Insert** | 1856; valid for a selected Smart Insert feature; in the graphics area, *feat* **RMB menu > Edit Smart Insert** |
| **swCommands\_Edit\_Suppress\_All\_Configs** | 1417; valid for a selected feature that has multiple configurations; **Edit menu > Suppress > All Configurations** |
| **swCommands\_Edit\_Suppress\_Feature** | 2498; valid for suppressible macro features; *macro\_feature* **RMB menu > Suppress** |
| **swCommands\_Edit\_Suppress\_Select\_Configs** | 1419; valid for a selected feature that has multiple configurations; **Edit menu > Suppress > Specified Configurations** |
| **swCommands\_Edit\_Swift\_Schema** | 2018; valid for a selected scheme in DimXpertManager, opens the Tolerance Scheme Properties PropertyManager page; in the DimXpertManager, *sel\_scheme* **RMB menu > Properties** |
| **swCommands\_Edit\_Template** | 1501; valid for drawings; **Sheet Format toolbar > Edit Sheet Format** |
| **swCommands\_Edit\_Text** | 1811; valid for a selected note annotation; **RMB menu > Edit Text** |
| **swCommands\_Edit\_Undolist** | 813; **Standard toolbar > Undo** |
| **swCommands\_Edit\_Unsuppress\_All\_Configs** | 1421; valid for a suppressed selected feature that has multiple configurations; **Edit menu > Unsuppress > All Configurations** |
| **swCommands\_Edit\_Unsuppress\_Dependent\_All\_Configs** | 1424; valid for a suppressed selected feature that has multiple configurations; **Edit menu > Unsuppress with Dependents > All Configurations** |
| **swCommands\_Edit\_Unsuppress\_Dependent\_Select\_Configs** | 1425; valid for a suppressed selected feature that has multiple configurations; **Edit menu > Unsuppress with Dependents > Specified Configurations** |
| **swCommands\_Edit\_Unsuppress\_Feature** | 2499; valid for suppressed macro features; *macro\_feature* **RMB menu > Unsuppress** |
| **swCommands\_Edit\_Unsuppress\_Select\_Configs** | 1422; valid for a suppressed selected feature that has multiple configurations; **Edit menu > Unsuppress > Specified Configurations** |
| **swCommands\_Edit\_Userdefined\_Start\_At\_Point** | 3167; valid for the SOLIDWORKS Routing add-in and an open routing assembly; **User Defined Route toolbar > Edit Route** |
| **swCommands\_Edit\_Vsection** | 1129; valid for a Section view; **View menu > Modify > Section View** |
| **swCommands\_Edit\_Weldment\_Props** | 2360; valid for weldments; in the FeatureManager design tree, **Weldment RMB menu > Properties** |
| **swCommands\_EditBlock** | 471; valid for models with blocks; **Blocks toolbar > Edit Block** |
| **swCommands\_EditColor** | 170; valid for a selected curve or sketch; **View toolbar > Edit Sketch or Curve Color** |
| **swCommands\_EditComponent** | 119; valid for a selected assembly component; **Assembly toolbar > Edit Component** |
| **swCommands\_EditFeature** | 623; valid for parts with features, **Edit Menu > Definition**; valid in many context toolbars, e.g., in the FeatureManager design tree, *feat\_name* **RMB context toolbar > Edit Feature**; valid for models with design tables; in the ConfigurationManager, **Tables folder > Design Table RMB menu > Edit Feature** |
| **swCommands\_EditFlexiblePartComp** | 3421; valid for the selected flexible assembly component; **RMB menu > Edit Flexible Part References** |
| **swCommands\_EditMacro** | 84; **Macro toolbar > Edit Macro** |
| **swCommands\_EditMaterial** | 501; valid for a selected part in an assembly; **Standard toolbar > Edit Material** |
| **swCommands\_Edt\_Elec\_Route** | 2251; valid for the SOLIDWORKS Routing add-in and an open routing assembly; **Electrical toolbar > Edit Route** |
| **swCommands\_Elec\_Rt\_Properties** | 2253; valid for the SOLIDWORKS Routing add-in and an open routing assembly; **Electrical toolbar > Route Properties** |
| **swCommands\_Electrical\_Autoroute** | 2079; valid for the SOLIDWORKS Routing add-in and an open routing assembly; **Routing Tools toolbar > Auto Route** |
| **swCommands\_Electrical\_EditConnector** | 3143; valid for the SOLIDWORKS Routing add-in and an open route; **Electrical toolbar > Edit Connectors** |
| **swCommands\_Electrical\_Load\_From\_To\_Data** | 2078; valid for the SOLIDWORKS Routing add-in and an open route; **Electrical toolbar > Edit Wires** |
| **swCommands\_Electrical\_Route** | 2271; valid for the SOLIDWORKS Routing add-in; **Routing toolbar > Electrical** |
| **swCommands\_Ellipse** | 87; valid in an open sketch; **Sketch toolbar > Ellipse** |
| **swCommands\_EmptyView** | 351; valid for drawings; **Drawing toolbar > Empty View** |
| **swCommands\_Enable\_Ann\_View\_Mode** | 2443; valid for parts and assemblies; in the FeatureManager design tree, **Annotations folder RMB menu > Enable Annotation View Visibility** |
| **swCommands\_End\_Contour\_Single\_Select** | 661; valid for parts or assemblies in contour single select mode, ends contour single select mode |
| **swCommands\_End\_Select\_Contour** | 2496; valid when a PropertyManager page is open, and **RMB menu > Start Contour Selection** was selected; in the graphics area, **RMB menu > End Select Contours** |
| **swCommands\_End\_Smart\_Selection** | 2629; valid during Smart selection; **RMB menu > End Smart Selection** |
| **swCommands\_EndCap** | 570; valid for weldments; **Weldments toolbar > End Cap** |
| **swCommands\_EndTreatment** | 517; valid for drawings with a selected edge; **Annotation toolbar > End Treatment** |
| **swCommands\_EnterTheOffsetOfTheSupportArea** | 6; alternative to swCommands\_Toolbar\_Table; **View menu > Toolbars > Table** |
| **swCommands\_Entity\_Properties** | 807; *entity* **RMB menu >** *entity* **Properties** |
| **swCommands\_Envelope\_Publisher** | 3416; **Tools toolbar > Envelope Publisher** |
| **swCommands\_Equations** | 51; **Tools toolbar > Equations** |
| **swCommands\_Escape\_Key\_Down** | 961; virtual key ESC |
| **swCommands\_ExcelBasedBillOfMaterials** | 512; valid for a selected view in a drawing of an assembly; **Table toolbar > Excel based Bill of Materials** |
| **swCommands\_Exit\_Measure** | 2961; Measure dialog > **Exit measure** |
| **swCommands\_Exit\_Sketch** | 862; valid for an open sketch; **RMB menu > Exit Sketch** |
| **swCommands\_Exit\_Structural\_Member** | 3404; valid when creating a structure system, exits from Advanced Structure System mode; **Structure System toolbar > Exit Structure System** |
| **swCommands\_Explode\_Add\_To\_Group** | 2544; valid when the Explode PropertyManager page is open, an explode step exists, and a component is selected; in the Explode PropertyManager page, **Explode Steps > Explode Step  >** *comp* **> RMB menu > Group** |
| **swCommands\_Explode\_Delete** | 2540; valid when the Explode PropertyManager page is open, and a group of chained explode steps exists; in the Explode PropertyManager page, **Explode Steps > Chain > Group >** *comp* **> RMB menu > Delete** |
| **swCommands\_Explode\_Delete\_Last\_Step** | 2545; valid when the Explode PropertyManager page is open, and a subassembly is selected; in the graphics area, **RMB menu > Delete from last step** |
| **swCommands\_Explode\_Done\_With\_Step** | 3385; valid when the Explode PropertyManager page is open, and a subassembly is selected; in the graphics area, **RMB menu > Done with step** |
| **swCommands\_Explode\_Move\_After\_Group\_T** | 2550; valid when the Explode PropertyManager page is open, and a group of chained explode steps exists; in the Explode PropertyManager page, **Explode Steps > Chain > Group >** *comp* **> RMB menu > Ungroup and move down** |
| **swCommands\_Explode\_Move\_Before\_Group\_T** | 2546; valid when the Explode PropertyManager page is open, and a group of chained explode steps exists; in the Explode PropertyManager page, **Explode Steps > Chain > Group >** *comp* **> RMB menu > Ungroup and move up** |
| **swCommands\_Explode\_Reuse\_Sub** | 2547; valid when the Explode PropertyManager page is open, and a subassembly is selected; in the graphics area, **RMB menu > Reuse subassembly explode** |
| **swCommands\_Explode\_Reuse\_Tree\_Sub** | 2549; valid when the Explode PropertyManager page is open, and a subassembly is selected; in the Explode PropertyManager page, **Explode Steps >** *subassembly* **RMB menu > Reuse subassembly explode** |
| **swCommands\_Explode\_Roll\_Back** | 3339; valid in an assembly's Exploded ViewN PropertyManager, **Explode Steps >** *explode\_stepN***RMB menu > Roll back** |
| **swCommands\_Explode\_Roll\_Forward** | 3340; valid in an assembly's Exploded ViewN PropertyManager, **Explode Steps >** *explode\_stepN***RMB menu > Roll forward** |
| **swCommands\_Explode\_Roll\_To\_End** | 3342; valid in an assembly's Exploded ViewN PropertyManager, **Explode Steps >** *explode\_stepN***RMB menu > Roll to end** |
| **swCommands\_Explode\_Roll\_To\_Previous** | 3341; valid in an assembly's Exploded ViewN PropertyManager, **Explode Steps >** *explode\_stepN***RMB menu > Roll to previous** |
| **swCommands\_Explode\_Suppress** | 3348; valid in an assembly's Exploded ViewN PropertyManager, **Explode Steps >** *explode\_stepN***RMB menu > Suppress** |
| **swCommands\_Explode\_Tree\_Edit** | 2553; valid when the Explode PropertyManager page is open, and a drag manipulator is selected; in the graphics area, *drag\_manip* **RMB menu > Edit step** |
| **swCommands\_Explode\_Unsuppress** | 3349; valid in an assembly's Exploded ViewN PropertyManager, **Explode Steps >** *explode\_stepN***RMB menu > Unsuppress** |
| **swCommands\_Explode\_Update\_Sub** | 2548; valid when the Explode PropertyManager page is open, and a subassembly's explode has been reused ; in the Explode PropertyManager, **Explode Steps >** *steps\_of\_subassembly* **RMB menu > Update subassembly's steps** |
| **swCommands\_ExplodeBlock** | 472; valid for blocks created in assembly layouts or drawings; **Layout Tools toolbar > Explode Block** |
| **swCommands\_ExplodedView** | 135; valid for assemblies; **Assembly toolbar > Exploded View** |
| **swCommands\_ExplodeLineSketch** | 395; valid for assemblies with exploded views; **Assembly toolbar > Explode Line Sketch** |
| **swCommands\_ExplodeSketch** | 485; alternative to swCommands\_Toolbar\_Exploderoute; **View menu > Toolbars > Explode Sketch** |
| **swCommands\_ExtendEntities** | 63; valid for open sketches; **Sketch toolbar > Extend Entities** |
| **swCommands\_ExtendSurface** | 301; valid for selected edge or face of a surface sketch; **Surfaces toolbar > Extend Surface** |
| **swCommands\_Extrude** | 392; valid only for parts; **2D to 3D toolbar > Convert to Extrusion** |
| **swCommands\_ExtrudedBossBase** | 8; valid for parts with a selected sketch; **Features toolbar > Extruded Boss/Base** |
| **swCommands\_ExtrudedCut** | 10; valid for parts; **Sheet Metal toolbar > Extruded Cut** or **Features toolbar > Extruded Cut** |
| **swCommands\_ExtrudedSurface** | 106; valid for a selected part sketch; **Surfaces toolbar > Extruded Surface** |
| **swCommands\_Face\_Curvature** | 1141; valid for parts or assemblies; alternative to swCommands\_Curvature; **View toolbar > Curvature** |
| **swCommands\_FaceCurves** | 321; valid for parts with a selected face; **Sketch toolbar > Face Curves** |
| **swCommands\_Far\_Stack\_Smart\_Fastener** | 2455; valid for a Smart Hole Fastener in an assembly; *smart\_hole\_fastener\_tree\_item* **RMB >** **Bottom stack** |
| **swCommands\_Feat\_Edit** | 865; valid for some selected surfaces and body features; in the graphics area, **RMB menu > Edit** |
| **swCommands\_Feature\_Color** | 651; in the FeatureManager design tree, *sketch\_name* **RMB menu > Sketch Color** |
| **swCommands\_Feature\_Pop\_Make\_Weld\_Bead** | 2391; valid for weldments with a selected feature; in the FeatureManager design tree, *feature\_name* **RMB menu > Make Weld Bead** |
| **swCommands\_Feature\_Pop\_Remove\_Weld\_Bead** | 2393; valid for weldments with a selected feature having weld beads; in the FeatureManager design tree, *feature\_name* **RMB menu > Make Non Weld Bead** |
| **swCommands\_Feature\_Pop\_Suppress\_Weld\_Beads** | 2392; valid for a selected weldment; in the FeatureManager design tree, **Weldment RMB menu > Suppress Weld Beads** |
| **swCommands\_Feature\_Pop\_Unsuppress\_Weld\_Beads** | 2394; valid for a selected weldment; in the FeatureManager design tree, **Weldment RMB menu > Unsuppress Weld Beads** |
| **swCommands\_Feature\_RV\_Appearance** | 2897; valid for parts or assemblies with a selected feature; in the FeatureManager design tree, *feature\_name* **RMB context toolbar > Appearances** > *feature\_name* |
| **swCommands\_Feature\_Texture** | 652; valid for a selected feature, opens the Texture PropertyManager page |
| **swCommands\_FeatureImportDiagnosis** | 70; valid for imported geometry only;  **Tools toolbar  > Import Diagnostics** |
| **swCommands\_Features** | 479; alternative to swCommands\_Toolbar\_Features; **View menu > Toolbars > Features** |
| **swCommands\_Featureworks** | 438; **SOLIDWORKS Add-ins toolbar > FeatureWorks** |
| **swCommands\_File\_Copy\_Design** | 2295; **File menu > Pack and Go** |
| **swCommands\_File\_Derive\_Comp** | 992; valid for assemblies; **File menu > Derive Component Part** |
| **swCommands\_File\_Find** | 977; **File menu > Find References** |
| **swCommands\_File\_Summaryinfo** | 963; **Standard toolbar > File Properties** |
| **swCommands\_FileClose** | 2789; **File menu > Close** or **Standard toolbar > Close** |
| **swCommands\_FileReload** | 113; **File menu > Reload** or **Standard toolbar > Reload** |
| **swCommands\_Fillet** | 9; valid for parts; **Features toolbar > Fillet** |
| **swCommands\_FilletBead** | 505; valid for weldments with two preselected face sets and one preselected intersecting edge set; **Weldment toolbar > Fillet Bead** |
| **swCommands\_FillPattern** | 558; valid for parts with a selected sketch; **Features toolbar > Fill Pattern** |
| **swCommands\_Filter\_Toolbar** | 1609; alternative to swCommands\_Toolbar\_Sel\_Filter; **View menu > Toolbars > Selection Filter** |
| **swCommands\_FilterAxes** | 279; **Selection Filter toolbar > Filter Axes** |
| **swCommands\_FilterBlocks** | 361; **Selection Filter toolbar > Filter Blocks** |
| **swCommands\_FilterCenterlines** | 441; **Selection Filter toolbar > Filter Centerlines** |
| **swCommands\_FilterCenterMarks** | 284; **Selection Filter toolbar > Filter Center Marks** |
| **swCommands\_FilterConnectionPoints** | 458; **Selection Filter toolbar > Filter Connection Points** |
| **swCommands\_FilterCosmeticThreads** | 292; **Selection Filter toolbar > Filter Cosmetic Threads** |
| **swCommands\_FilterDatumFeatures** | 289; **Selection Filter toolbar > Filter Datum Features** |
| **swCommands\_FilterDatumTargets** | 291; **Selection Filter toolbar > Filter Datum Targets** |
| **swCommands\_FilterDimensionsHoleCallouts** | 285; **Selection Filter toolbar > Filter Dimensions/Hole Callouts** |
| **swCommands\_FilterDowelPinSymbols** | 382; **Selection Filter toolbar > Filter Dowel Pin Symbols** |
| **swCommands\_FilterEdges** | 277; **Selection Filter toolbar > Filter Edges** |
| **swCommands\_FilterFaces** | 278; **Selection Filter toolbar > Filter Faces** |
| **swCommands\_FilterGeometricTolerances** | 287; **Selection Filter toolbar > Filter Geometric Tolerances** |
| **swCommands\_FilterMeshFacet** | 3230; allows selection of mesh facets only; **Selection Filter toolbar > Filter Mesh Facets** |
| **swCommands\_FilterMeshFin** | 3231; allows selection of mesh facet edges only; **Selection Filter toolbar > Filter Mesh Facet Edges** |
| **swCommands\_FilterMeshVertex** | 3232; allows selection of mesh facet vertices only; **Selection Filter toolbar > Filter Mesh Facet Vertices** |
| **swCommands\_FilterMidpoints** | 283; **Selection Filter toolbar > Filter Midpoints** |
| **swCommands\_FilterNotesBalloons** | 288; **Selection Filter toolbar > Filter Notes/Balloons** |
| **swCommands\_FilterPlanes** | 280; **Selection Filter toolbar > Filter Planes** |
| **swCommands\_FilterRoutingPoints** | 459; **Selection Filter toolbar > Filter Routing Points** |
| **swCommands\_FilterSketches** | 2857; **Selection Filter toolbar > Filter Sketches** |
| **swCommands\_FilterSketchPoints** | 281; **Selection Filter toolbar > Filter Sketch Points** |
| **swCommands\_FilterSketchSegments** | 282; **Selection Filter toolbar > Filter Sketch Segments** |
| **swCommands\_FilterSolidBodies** | 419; **Selection Filter toolbar > Filter Solid Bodies** |
| **swCommands\_FilterSurfaceBodies** | 303; **Selection Filter toolbar > Filter Surface Bodies** |
| **swCommands\_FilterSurfaceFinishSymbols** | 286; **Selection Filter toolbar > Filter Surface Finish Symbols** |
| **swCommands\_FilterVertices** | 276; **Selection Filter toolbar > Filter Vertices** |
| **swCommands\_FilterWeldBeads** | 577; **Selection Filter toolbar > Filter Weld Beads** |
| **swCommands\_FilterWeldSymbols** | 290; **Selection Filter toolbar > Filter Weld Symbols** |
| **swCommands\_Final\_Render** | 2969; **Render Tools toolbar > Final Render** |
| **swCommands\_Find\_Next** | 764; dialog resource **Find Next** |
| **swCommands\_Finish\_Active\_Contour** | 665; valid for an active sketch in contour manipulation mode; in the graphics area, **RMB menu > Finish Contour** |
| **swCommands\_FitSpline** | 426; valid for a sketch in edit mode; **Spline Tools toolbar > Fit Spline** |
| **swCommands\_FitText** | 628; valid for selected text; **Formatting toolbar > Fit Text** |
| **swCommands\_Fix\_Component** | 957; valid for a selected floating component; in the FeatureManager design tree, *comp* **RMB menu > Fix** |
| **swCommands\_Fixed\_Length\_Covering** | 3382; valid for SOLIDWORKS Routing add-in and an open assembly with a route and selected route segments; **Routing Tools toolbar > Fixed Length Covering** |
| **swCommands\_Fixed\_Length\_Route** | 3149; valid for SOLIDWORKS Routing add-in and an open assembly with a route and selected route segments; **Routing Tools toolbar > Fixed Length** |
| **swCommands\_FlatPatternBendNotch** | 3529; **Insert > Sheet Metal > Bend Notch...** |
| **swCommands\_Flatten** | 138; valid for sheet metal parts; **Sheet Metal toolbar > Flatten** |
| **swCommands\_Flex** | 409; valid for parts; **Features toolbar > Flex** |
| **swCommands\_Flex\_Tube\_Rt\_Properties** | 2261; valid for the SOLIDWORKS Routing add-in and an open flexible tubing assembly; **Flexible Tubing toolbar > Route Properties** |
| **swCommands\_Flexible\_Part\_Remove\_Ref** | 3430; valid for a selected reference entity in the Flexible References group box of the Activate Flexible Component PropertyManager; **selected PM reference entity RMB menu > Delete** |
| **swCommands\_Flexible\_Tube\_Route** | 2272; valid for the SOLIDWORKS Routing add-in; **Routing toolbar > Flexible Tube** |
| **swCommands\_Flip\_Direction** | 2560; valid in sketch constraint list boxes; list\_box **RMB menu > Flip Relation** |
| **swCommands\_Flip\_Dowel\_Sym** | 1806; valid for a selected dowel symbol; *dowel\_sym* **RMB menu > Flip Symbol** |
| **swCommands\_Flip\_Endpoint\_Tangency** | 3535; **Sketch toolbar > Flip Endpoint Tangent** |
| **swCommands\_Flip\_Ref\_Dim** | 1548; *selected\_reference\_dimension* **RMB menu > Change Plane** |
| **swCommands\_Flip\_Smart\_Fastener** | 2453; valid only for Toolbox add-ins and assemblies and only when editing a Smart Fastener grouping; in the Smart Fasteners PropertyManager page, **Results > Group1 > Series1** **RMB menu > Flip** |
| **swCommands\_FlowSimulation** | 3504; SOLIDWORKS Flow Simulation |
| **swCommands\_FlowSimulation\_ElCooling** | 3506; SOLIDWORKS Flow Simulation + Electronics |
| **swCommands\_FlowSimulation\_HVAC** | 3505; SOLIDWORKS Flow Simulation + HVAC |
| **swCommands\_FlowSimulation\_HVAC\_ElCooling** | 3507; SOLIDWORKS Flow Simulation + HVAC + Electronics |
| **swCommands\_Fmt\_Painter** | 2841; valid for a selected annotation or dimension from which to copy visual properties; **Tools toolbar > Format Painter** |
| **swCommands\_Fmt\_Painter\_Apply\_All** | 2856; valid after calling swCommands\_Fmt\_Painter (Format Painter) and selecting the annotation or dimension to copy from; in the graphics area, *selected\_anno\_or\_dim* **RMB menu > Apply to all** |
| **swCommands\_Fold** | 325; valid for sheet metal parts; **Sheet Metal toolbar > Fold** |
| **swCommands\_Font\_Continue\_Number** | 2099; **Text editor popup menu > Continue Numbering** |
| **swCommands\_Font\_Face** | 1148; valid for selected text; **Formatting toolbar > Document Font (dropdown)** |
| **swCommands\_Font\_Points** | 1150; valid for selected text; **Formatting toolbar > Font Points (dropdown)** |
| **swCommands\_Font\_Restart\_Number** | 2098; **Text editor popup menu > Restart Numbering** |
| **swCommands\_Font\_Units** | 1149; valid for selected text; **Formatting toolbar > Font Units** |
| **swCommands\_Fonts** | 480; alternative to swCommands\_Toolbar\_Font; **View menu > Toolbars > Formatting** |
| **swCommands\_Force\_Regen\_Bucket** | 3501; Regenerates drawing views; CTRL-Shift-Q |
| **swCommands\_ForceMateMisalignment** | 3326; valid for a pre-selected concentric mate, forces misalignment; in the FeatureManager design tree, concentric mate **RMB menu > Force misalignment** |
| **swCommands\_Form\_Newassembly** | 1259; valid for assemblies with one or more selected components or feature foldesr; in the FeatureManager design tree, *sel\_comp* **RMB menu > Form New Subassembly** |
| **swCommands\_FormingTool** | 560; valid for sheet metal parts; **Sheet Metal toolbar > Forming Tool** |
| **swCommands\_Forward** | 1615; **palette toolbar > Forward** |
| **swCommands\_FourView** | 552; **View toolbar > Four View** |
| **swCommands\_Freeze\_All** | 3015; valid for a selected freeze bar in the FeatureManager design tree; *freeze\_bar* **RMB menu > Roll to End (Freeze All)** |
| **swCommands\_Front** | 161; **View toolbar > View Orientation > Front** |
| **swCommands\_FullScreenMode** | 619; F11 or **View menu > Full Screen** or **Standard toolbar > Full Screen View** |
| **swCommands\_FullyDefineSketch** | 600; valid for an open sketch; **Dimensions/Relations toolbar > Fully Define Sketch** |
| **swCommands\_Gantt\_Zoomin** | 2146; **Motion Study Animator toolbar > Zoom In** |
| **swCommands\_Gantt\_Zoomout** | 2147; **Motion Study Animator toolbar > Zoom Out** |
| **swCommands\_Gantt\_Zoomtofit** | 2916; **Motion Study Animator toolbar > Zoom to Fit** |
| **swCommands\_GeneralTable** | 412; valid for drawings; **Table toolbar > General Table** |
| **swCommands\_GeneralToleranceTable** | 3233; valid for drawings; **Table toolbar > General Tolerance Table** |
| **swCommands\_Generate\_Region** | 2510; valid during contour selection if region selection is enabled, **RMB menu > Generate Regions** |
| **swCommands\_Geometric\_Callout** | 1838; valid for a selected hole wizard callout dimension; **RMB menu > Define by Geometry** |
| **swCommands\_GeometricTolerance** | 58; valid for drawings; **Annotation toolbar > Geometric Tolerance** |
| **swCommands\_GetSupport** | 3446; **Help > Get Support** |
| **swCommands\_Glassbox\_Done** | 2196; valid after running swCommands\_3DDrawingView for a selected drawing view; **OK** in popup toolbar dialog |
| **swCommands\_Glassbox\_Exit** | 2986; valid after running swCommands\_3DDrawingView for a selected drawing view; **Exit** in popup toolbar dialog |
| **swCommands\_Glassbox\_Pan** | 2201; valid after running swCommands\_3DDrawingView for a selected drawing view; **Pan** in popup toolbar dialog |
| **swCommands\_Glassbox\_Rotate** | 2200; valid after running swCommands\_3DDrawingView for a selected drawing view; **Rotate** in popup toolbar dialog |
| **swCommands\_Glassbox\_Save** | 2987; valid after running swCommands\_3DDrawingView for a selected drawing view; **Save the view** in popup toolbar dialog |
| **swCommands\_Glassbox\_ViewOrient** | 2988; valid after running swCommands\_3DDrawingView for a selected drawing view; **View Orientation** in popup toolbar dialog |
| **swCommands\_Glassbox\_Zoom** | 2199; valid after running swCommands\_3DDrawingView for a selected drawing view; **Zoom in/out** in popup toolbar dialog |
| **swCommands\_Glassbox\_Zoomto** | 2198; valid after running swCommands\_3DDrawingView for a selected drawing view; **Zoom to Area** in popup toolbar dialog |
| **swCommands\_Glassbox\_Zoomtofit** | 2197; valid after running swCommands\_3DDrawingView for a selected drawing view; **Zoom to Fit** in popup toolbar dialog |
| **swCommands\_Go\_To\_Mate\_Component\_1** | 2528; valid for assemblies with mate components; in the FeatureManager design tree, *first\_part\_mate\_relation* **RMB menu >** *second\_part\_mate* **> Go to** |
| **swCommands\_Go\_To\_Mate\_Component\_2** | 2533; valid for assemblies with mate components; in the FeatureManager design tree, second*\_part\_mate\_relation* **RMB menu >** *first\_part\_mate* **> Go to** |
| **swCommands\_Goto\_Auxiliary\_View** | 1404; valid for drawings with an auxiliary view; in the drawing, *selected\_auxiliary\_view\_arrow* **RMB menu > Jump to Auxiliary View** |
| **swCommands\_Goto\_Component** | 1587; valid for assembly views under special circumstances; in the graphics view, *comp* **RMB menu > Go to Component (in Tree)** |
| **swCommands\_Goto\_Detail\_View** | 1402; valid for drawings with a detail view; in the drawing, *detail\_circle* **RMB menu > Jump to Detail View** |
| **swCommands\_Goto\_Feature** | 1586; in the graphics area, *selected\_entity* **RMB menu > Go to Feature (in Tree)** |
| **swCommands\_Goto\_Parent\_View** | 1403; valid for drawings with a section or detail view; *detail\_view* **RMB menu > Jump to Parent View** |
| **swCommands\_Goto\_Projected\_View** | 1405; valid for drawings with a projected view; *projected\_view\_arrow* **RMB menu > Jump to Projected View** |
| **swCommands\_Goto\_Section\_View** | 1401; valid for drawings with a section view; section*\_view\_arrow* **RMB menu > Jump to Section View** |
| **swCommands\_Gravity** | 420; valid in the context of  Basic Motion Studies; in the MotionManager toolbar, **Gravity** adds gravity to a motion study |
| **swCommands\_Grid\_Align** | 673; resource string or dialog resource **Align Grid** |
| **swCommands\_Grid\_View** | 2999; valid for a part or assembly with a GridSystem feature; in the FeatureManager design tree, *grid\_system* **RMB menu > View Grid Components** |
| **swCommands\_GridFeature** | 2982; valid for parts or assemblies; **Features toolbar** **> Grid System** or **Insert > Reference Geometry > Grid System** |
| **swCommands\_GridSnap** | 41; valid for sketches; **Quick Snaps toolbar > Grid Snap** |
| **swCommands\_GrooveWeld** | 3530; valid for parts, adds a groove weld bead feature between two selected disjoint bodies; **Insert > Weldments > Groove Bead** |
| **swCommands\_Ground\_Plane** | 3217; valid for assemblies only, opens the Ground Plane PropertyManage page; **Insert menu > Reference Geometry > Ground Plane** |
| **swCommands\_Group** | 318; valid for multi-selected annotations or dimensions in a drawing; **Align toolbar > Group** |
| **swCommands\_Group\_Remove\_Item** | 1455; valid for a drawing with a group of three or more annotations or dimensions; *grouped\_anno* **RMB menu > Group > Remove from Group** |
| **swCommands\_Gusset** | 453; valid for weldments with two selected adjoining faces; **Weldments toolbar > Gusset** |
| **swCommands\_HandSketch** | 2850; valid only for a sketch opened in SOLIDWORKS running on supporting pen/stylus hardware;**Sketch Ink toolbar > Insert HandSketch** |
| **swCommands\_HandsketchColor** | 3238; valid only on supporting pen/stylus hardware, sets pen stroke color; **Sketch Ink** **toolbar > Color** |
| **swCommands\_HandsketchConvertEntity** | 3241; valid only on supporting pen/stylus hardware, automatically converts a pen stroke to sketch entities; **Sketch Ink****toolbar > Auto Convert to Entities** |
| **swCommands\_HandsketchConvertShape** | 3240; valid only on supporting pen/stylus hardware, automatically converts a pen stroke to recognized shapes; **Sketch Ink****toolbar > Auto Convert to Shape** |
| **swCommands\_HandsketchDraw** | 3455; valid only on supporting pen/stylus hardware, draws ink strokes; ****Sketch Ink** toolbar > Pen** |
| **swCommands\_HandsketchEditModify** | 3413; valid only on supporting pen/stylus hardware, edit power modify sketch entities; **Sketch Ink toolbar > Edit Power Modify** |
| **swCommands\_HandsketchEraser** | 3236; valid only on supporting pen/stylus hardware, erases pen strokes; ****Sketch Ink** toolbar > Eraser** |
| **swCommands\_HandsketchModify** | 3409; valid only on supporting pen/stylus hardware, modifies the sketch; **Sketch Ink toolbar > Power Modify** |
| **swCommands\_HandsketchPen** | 3235; valid only on supporting pen/stylus hardware, uses pen for sketch ink; **Tools menu > Sketch Tools > Pen Tools > Pen** |
| **swCommands\_HandsketchPenProps** | 3295; valid only on supporting pen/stylus hardware, gets pen properties; **Sketch Ink toolbar > Pen** or **Tools > Sketch Settings > Pen Settings > Pen Properties** |
| **swCommands\_HandsketchProtractor** | 3381; valid only on supporting pen/stylus hardware, toggles the pen sketch protractor; **Sketch Ink toolbar > Protractor** |
| **swCommands\_HandsketchReplaceChamfer** | 3426; valid only on supporting pen/stylus hardware, converts power modify to sketch chamfer; **Sketch Ink toolbar > Convert to Sketch Chamfer** |
| **swCommands\_HandsketchReplaceComposite** | 3345; valid only on supporting pen/stylus hardware, converts recognized shape with Composite; **Sketch Ink toolbar > Convert to Composite** |
| **swCommands\_HandsketchReplaceEllipse** | 3347; valid only on supporting pen/stylus hardware, converts recognized shape with Ellipse; **Sketch Ink toolbar > Convert to Ellipse** |
| **swCommands\_HandsketchReplaceExtend** | 3428; valid only on supporting pen/stylus hardware, converts power modify to sketch extend; **Sketch Ink toolbar > Convert to Sketch Extend** |
| **swCommands\_HandsketchReplaceFillet** | 3427; valid only on supporting pen/stylus hardware, converts power modify to sketch fillet; **Sketch Ink toolbar > Convert to Sketch Fillet** |
| **swCommands\_HandsketchReplaceSlot** | 3346; valid only on supporting pen/stylus hardware, converts recognized shape with Slot; **Sketch Ink toolbar > Convert to Slot** |
| **swCommands\_HandsketchReplaceSpline** | 3344; valid only on supporting pen/stylus hardware, converts recognized shape with Spline; **Sketch Ink toolbar > Convert to Spline** |
| **swCommands\_HandsketchRuler** | 3291; valid only on supporting pen/stylus hardware, toggles the pen sketch ruler; **Sketch Ink toolbar > Ruler** |
| **swCommands\_HandsketchSelect** | 3237; valid only on supporting pen/stylus hardware, uses the pen to select; **Sketch Ink toolbar > Select** |
| **swCommands\_HandsketchSplineMode** | 3387; valid only on supporting pen/stylus hardware, automatically converts complex stroke to spline; **Sketch Ink toolbar > Auto Spline** |
| **swCommands\_HandsketchTouch** | 3290; valid only on supporting pen/stylus hardware, toggles Touch input to Pen Sketch; **Sketch Ink toolbar > Touch** |
| **swCommands\_HandsketchUpdateToEntity** | 3241; valid only on supporting pen/stylus hardware, updates the selected pen stroke to sketch entities; **Sketch Ink toolbar > Update to Entities** |
| **swCommands\_HandsketchUpdateToShape** | 3240; valid only on supporting pen/stylus hardware, updates the selected pen stroke to a recognized shape; **Sketch Ink toolbar > Update to Shape** |
| **swCommands\_Hatch\_Properties** | 674; valid for hatched section views in drawings or part sketches; *selected\_hatched\_sketch* **RMB menu > Crosshatch Properties** |
| **swCommands\_HealEdges** | 518; valid for parts for selected faces; **Features toolbar > Heal Edges** |
| **swCommands\_Helix\_Ccw** | 2389; valid when the Helix/Spiral PropertyManager page is open, and the helix is going clockwise; in the graphics area, **RMB menu > Counterclockwise** |
| **swCommands\_Helix\_Cw** | 2387; valid when the Helix/Spiral PropertyManager page is open, and the helix is going counterclockwise; in the graphics area, **RMB menu > Clockwise** |
| **swCommands\_Helix\_Taperhelix** | 2388; valid when the Helix/Spiral PropertyManager page is open; in the graphics area, **RMB menu > Taper Helix** |
| **swCommands\_HelixAndSpiral** | 94; valid for parts with a selected sketch of a single circle; **Features toolbar > Curves > Helix and Spiral** |
| **swCommands\_Helixdve\_Revdir** | 2386; valid when the Helix/Spiral PropertyManager page is open, and the helix is going counterclockwise; in the graphics area, **RMB menu > Reverse Direction** |
| **swCommands\_Help** | 340; **Standard toolbar > Help** |
| **swCommands\_Help\_Autocad\_Users** | 1882; **Help menu > Moving from 2D to 3D** |
| **swCommands\_Help\_Onlinetutorial** | 1423; **Help menu > SOLIDWORKS Tutorials** |
| **swCommands\_Hem** | 363; valid for sheet metal parts; **Sheet Metal toolbar > Hem** |
| **swCommands\_HiddenLinesRemoved** | 335; **View toolbar > Display Style > Hidden Lines Removed** |
| **swCommands\_HiddenLinesVisible** | 336; **View toolbar > Display Style > Hidden Lines Visible** |
| **swCommands\_Hide\_3d\_Sketch\_Triad** | 3528; valid for an open 3D sketch displaying the sketcher triad; in the graphics area, **RMB menu > Hide Sketcher Triad** |
| **swCommands\_Hide\_Bom** | 1239; valid for a drawing view excel-based BOM; *excel\_based\_bom* **RMB menu > Hide** |
| **swCommands\_Hide\_Components** | 925; valid for selected components in assemblies; in the FeatureManager design tree, *selected\_comp* **RMB context toolbar > Hide Components** |
| **swCommands\_Hide\_Components\_All\_Configs** | 1649; valid for a selected top-level assembly; **Edit menu > Hide > All Display States** |
| **swCommands\_Hide\_Components\_Select\_Configs** | 1650; valid for a selected top-level assembly, opens the Apply To Display States dialog; **Edit menu > Hide > Specified Display States** |
| **swCommands\_Hide\_Cthread** | 1528; valid for a model with a selected cosmetic thread; in the graphics area, *cosmetic\_thread* **RMB context toolbar > Hide Cosmetic Thread** |
| **swCommands\_Hide\_Dim** | 1539; valid in drawings with annotations or dimension; in the graphics area, *selected\_anno* **RMB menu > Hide** |
| **swCommands\_Hide\_Dim\_Leader** | 2538; valid for a drawing with a dimension with a leader line; *leader\_line* **RMB menu > Hide Dimension Line** |
| **swCommands\_Hide\_Dim\_Witness** | 2526; valid for a drawing with a dimension with a witness line; *witness\_line* **RMB menu > Hide Extension Line** |
| **swCommands\_Hide\_Feature\_Detail** | 931; valid for a selected top-level assembly showing feature detail; in the graphics area, **RMB menu > Show Hierarchy Only** |
| **swCommands\_Hide\_Incontext\_Feature\_Holders** | 687; valid for a selected top-level assembly with visible update holders; *selected\_assembly* **RMB menu > Hide Update Holders** |
| **swCommands\_Hide\_Mate\_Component\_1** | 2529; valid for assemblies with visible mate components; in the FeatureManager design tree, *first\_part\_mate\_constraint* **RMB menu >** *second\_part\_mate* **> Hide component** |
| **swCommands\_Hide\_Mate\_Component\_2** | 2534; valid for assemblies with visible mate components; in the FeatureManager design tree, *second\_part\_mate\_constraint* **RMB menu >** *first\_part\_mate* **> Hide component** |
| **swCommands\_Hide\_Mesh\_Feat** | 3211; valid for a selected mesh feature that is visible; **RMB menu > Hide** |
| **swCommands\_Hide\_Sketch\_Dim\_In\_Drawing** | 2478; valid for a selected visible dimension in a drawing sketch; **RMB menu > Hide Dimensions** |
| **swCommands\_Hide\_Table** | 2623; valid for models with tables; in the FeatureManager design tree, *table\_name* **RMB menu > Hide Table** |
| **swCommands\_Hide\_Zone** | 1561; valid for assemblies with envelope components; in the FeatureManager design tree, *envelope\_feature* **RMB menu > Envelope > Select Using Envelope** |
| **swCommands\_HideEdge** | 353; valid for a selected edge in a drawing, hides the selected edge |
| **swCommands\_Hideshow\_Brwser\_Tree** | 2556; F9 or **View menu > User Interface > FeatureManager Tree Area** |
| **swCommands\_HideShowAnnotations** | 67; **Annotation toolbar > Hide/Show Annotations** |
| **swCommands\_HideShowComponents** | 85; valid for selected components in an assembly; **Assembly toolbar > Hide/Show Components** |
| **swCommands\_HideShowEdges** | 2938; valid for drawings; **Line Format toolbar > Hide/Show Edges** |
| **swCommands\_Hlink\_History** | 684; **Web toolbar >** *web\_history\_dropdown* |
| **swCommands\_Hole\_Table\_Expand\_Same\_Size** | 2368; valid for drawings with hole tables where same-size holes are combined; in the FeatureManager design tree, *hole\_table* **RMB menu > Expand Same Sizes** |
| **swCommands\_Hole\_Table\_Goto\_Tag** | 2364; valid for drawings with hole tables; in the drawing, *hole\_table\_cell* **RMB menu > Jump to Tag** |
| **swCommands\_Hole\_Table\_Hide\_Centers** | 2370; valid for drawings with hole tables whose hole centers are visible; in the drawing, *hole\_table* **RMB menu > Hide Hole Centers** |
| **swCommands\_Hole\_Table\_Hide\_Origin** | 2362; valid for drawings with hole tables whose hole origins are visible; in the drawing, *hole\_table* **RMB menu > Hide Origin Indicator** |
| **swCommands\_Hole\_Table\_Hide\_Tags** | 2438; valid for drawings with hole tables whose hole tags are visible; in the drawing, *hole\_table* **RMB menu > Hide Hole Tags** |
| **swCommands\_Hole\_Table\_Show\_Centers** | 2369; valid for drawings with hole tables whose hole centers are hidden; in the drawing, *hole\_table* **RMB menu > Show Hole Centers** |
| **swCommands\_Hole\_Table\_Show\_Origin** | 2363; valid for drawings with hole tables whose hole origins are hidden; in the drawing, *hole\_table* **RMB menu > Show Origin Indicator** |
| **swCommands\_Hole\_Table\_Show\_Tags** | 2437; valid for drawings with hole tables whose hole tags are hidden; in the drawing, *hole\_table* **RMB menu > Show Hole Tags** |
| **swCommands\_HoleAlignment** | 2822 valid for assemblies; **Assembly toolbar > Hole Alignment** |
| **swCommands\_HoleCallout** | 121; valid for drawings with holes or circular cut features; **Annotation toolbar > Hole Callout** |
| **swCommands\_HoleSeries** | 556; valid for assemblies with multi-selected part locations for a series of holes; **Features toolbar** or **Insert menu > Assembly Feature > Hole > Hole Series** |
| **swCommands\_HoleTable** | 446; valid for drawings; **Table toolbar > Hole Table** |
| **swCommands\_HoleWizard** | 39; valid for parts with a selected sketch, opens the Hole Specification PropertyManager page; **Features toolbar > Hole Wizard**; also valid for assemblies; **Insert menu > Assembly Feature > Hole > Wizard** |
| **swCommands\_Holewizard\_Callout** | 1839; valid for drawings with radial annotations; in the drawing, *radial\_dimension* **RMB menu > Display Options > Define by Hole Wizard** |
| **swCommands\_Home** | 1617; **palette toolbar > Home** |
| **swCommands\_HorizontalDimension** | 66; valid for open sketches; **Dimensions/Relations toolbar > Horizontal Dimension** |
| **swCommands\_HorizontalOrdinateDimension** | 347; valid for open sketches; **Dimensions/Relations toolbar > Horizontal Ordinate Dimension** |
| **swCommands\_HVPointSnap** | 522; valid for sketches; **Quick Snaps toolbar > H/V Point Snap** |
| **swCommands\_HVSnap** | 525; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; **Quick Snaps toolbar > H/V Snap** |
| **swCommands\_Ignore\_Construction\_Geom** | 3332; valid when the Trim PropertyManager is active, **graphics area RMB menu > Ignore trimming of construction geometry** |
| **swCommands\_Import\_To\_Drawing** | 1772; valid for a part with a location, basic location, or basic size dimension; *location\_dimension* **RMB menu > Mark for Drawing** |
| **swCommands\_ImportedGeometry** | 96; valid for parts; **Features toolbar > Imported Geometry** |
| **swCommands\_IncreaseIndent** | 544; valid for selected text; **Formatting toolbar > Increase indent** |
| **swCommands\_Indent** | 571; valid for multi-body parts with selected target and tool bodies; **Features toolbar > Indent** |
| **swCommands\_InkMarkupEraser** | 3441; valid only in Markup Views, erases ink strokes; **Markup toolbar > Erase** |
| **swCommands\_InkMarkupMouse** | 3440; valid only in Markup Views, draws with the mouse; **Markup toolbar > Draw** |
| **swCommands\_InkMarkupPen** | 3439; valid only on supporting pen/stylus hardware and only in Markup Views, uses pen for Markup Ink input; **Markup toolbar > Pen** |
| **swCommands\_InkMarkupPenProps** | 3438; valid only on supporting pen/stylus hardware and only in Markup Views, sets ink color and thickness; **Markup toolbar > Color** |
| **swCommands\_InkMarkupSelect** | 3442; valid only on supporting pen/stylus hardware and only in Markup Views, selects ink strokes or notes; **Markup toolbar > Select** |
| **swCommands\_InkMarkupText** | 3444; valid only on supporting pen/stylus hardware and only in Markup Views, adds a note to the current Markup View; **Markup toolbar > Note** |
| **swCommands\_InkMarkupView** | 3398; inserts a Markup View; **Markup toolbar > Markup View** |
| **swCommands\_Insert\_Baseline\_Dimension** | 3048; valid for a selected baseline dimension in a drawing; *baseline\_dim* **RMB menu > Add to BaseLine** |
| **swCommands\_Insert\_Bendtable\_New** | 1443; valid for a sheet metal part; **Insert menu > Bend Table > New** |
| **swCommands\_Insert\_Bendtable\_Open** | 1442; valid for a sheet metal part; **Insert menu > Bend Table > From File** |
| **swCommands\_Insert\_Camera** | 2191; valid for parts; in DisplayManager, **Scene, Lights, and Cameras > Camera RMB menu > Add Camera** |
| **swCommands\_Insert\_Chain\_Dimension** | 3405; starts the Chain Dimension tool; **Tools menu > Dimensions > Chain** |
| **swCommands\_Insert\_Connection\_Point** | 1223; valid for the SOLIDWORKS Routing add-in and an open routing assembly; **Routing toolbar > Connection Point** |
| **swCommands\_Insert\_Connector** | 2862; valid for the SOLIDWORKS Routing add-in and an open electrical routing assembly; **Electrical toolbar > Insert Connectors** |
| **swCommands\_Insert\_Create\_Assy\_Feat** | 1974; valid for parts with solid bodies; in the FeatureManager design tree, **Cut list or Solid bodies folder RMB menu > Save Bodies;** opens the Save Bodies PropertyManager |
| **swCommands\_Insert\_Cthread\_Callout** | 845; valid for drawing views with a selected cosmetic thread that was created without a standard and with non-empty Thread Callout text; in the drawing, *callout\_thread* **RMB menu > Insert Callout** |
| **swCommands\_Insert\_Custom\_Symbol\_Save** | 1208; *custom\_symbol* **RMB menu > Save to File** |
| **swCommands\_Insert\_Cut\_Net** | 2175; valid for parts with a selected sketch; **Features toolbar > Boundary Cut** |
| **swCommands\_Insert\_Drw\_Dxfdwg** | 1849; **Insert menu > DXF/DWG** |
| **swCommands\_Insert\_Feature\_Lock** | 29599; valid for models where feature freeze is enabled, and the feature to freeze is selected; in the FeatureManager design tree, *feature* **RMB menu > Freeze** |
| **swCommands\_Insert\_Ff\_View\_3rd** | 1244; valid when adding a 1st or 3rd angle view to a drawing; **RMB menu > Insert From File** |
| **swCommands\_Insert\_Folder** | 1829; valid for a selected item in the FeatureManager design tree; *feature\_name* **RMB menu > Add to New Folder** |
| **swCommands\_Insert\_Form\_Assembly** | 1325; valid for assemblies with selected components, opens Assembly Structure Editing dialog; **Insert menu > Component > Assembly from [Selected] Components** |
| **swCommands\_Insert\_From\_PartSupply** | 3498; Opens 3DEXPERIENCE PartSupply in the SOLIDWORKS Task Pane. Browse PartSupply’s comprehensive and intelligent catalog of qualified sourceable 3D components to add to your assembly; only valid if 3DEXPERIENCE Marketplace Add-in is loaded and logged into; **SOLIDWORKS menu > Insert > Component > Insert from PartSupply** |
| **swCommands\_Insert\_Geometry\_Import** | 1878; alternative to swCommands\_ImportedGeometry; **Features toolbar > Imported Geometry** |
| **swCommands\_Insert\_Light\_Distantlight** | 1295; in DisplayManager, **Scene, Lights, and Cameras > SOLIDWORKS Lights RMB menu > Add Directional Light** |
| **swCommands\_Insert\_Light\_Pointlight** | 1293; in DisplayManager, **Scene, Lights, and Cameras > SOLIDWORKS Lights RMB menu > Add Point Light** |
| **swCommands\_Insert\_Light\_Spotlight** | 1294; in DisplayManager, **Scene, Lights, and Cameras > SOLIDWORKS Lights RMB menu > Add Spot Light** |
| **swCommands\_Insert\_Light\_Sunlight** | 3093; in DisplayManager, **Scene, Lights, and Cameras > SOLIDWORKS Lights RMB menu > Add Sunlight** |
| **swCommands\_Insert\_Mirror\_Subassembly** | 1638; valid for assemblies; **Assembly toolbar > Mirror Components** |
| **swCommands\_Insert\_Mirrored\_Part** | 988; valid for parts with a selected plane about which to mirror the part; **Insert menu > Mirror Part** |
| **swCommands\_Insert\_Object** | 818; opens an Insert Object dialog; **Insert menu > Object** |
| **swCommands\_Insert\_Picture** | 1131; valid for assemblies, opens an Open dialog with a Tiff Images (\*.tif) selection filter; **Insert > Picture** |
| **swCommands\_Insert\_Ref\_Line** | 1212; opens a Reference Line dialog |
| **swCommands\_Insert\_Refdim** | 909; valid for drawings, activates the dimensioning cursor; after calling this command, select one or two edges/vertices and then a location where to place the reference dimension text |
| **swCommands\_Insert\_Route\_Point** | 1222; valid for the SOLIDWORKS Routing add-in, opens a Route Point PropertyManager page; **Routing Tools toolbar > Route Point** |
| **swCommands\_Insert\_Schematic** | 1632; valid for drawings, opens the Position Schematic PropertyManager page; **Insert menu > Schematic** |
| **swCommands\_Insert\_Sculpt** | 3051; valid for parts with two or more selected solid bodies; **Features toolbar >** **Intersect** |
| **swCommands\_Insert\_Sectionline** | 924; valid for a selected drawing sheet or view, opens a Make Section Line PropertyManager page; **Insert menu > Make Section Line** |
| **swCommands\_Insert\_Sheet** | 857; valid for drawings; **Insert menu > Sheet** |
| **swCommands\_Insert\_Sketch\_Dxfdwg** | 1833; valid for parts with a selected plane where to insert the drawing, opens an Open dialog with a Dxf Files (\*.dxf) filter; **Insert menu > DXF/DWG** |
| **swCommands\_Insert\_Sketch\_Import** | 1408; valid for an open (minimized) drawing and an active window with an open sketch in a part; **Insert menu > Sketch from Drawing** (see the SOLIDWORKS Help) |
| **swCommands\_Insert\_Smart\_Features** | 2220; valid for an assembly with a saved, selected Smart Component, opens the Smart Feature Insert PropertyManager page; **Insert menu > Smart Features;** in the FeatureManager design tree, *Smart\_Component* **RMB menu > Insert Smart Feature** |
| **swCommands\_Insert\_Smartfeature** | 2235; valid for assemblies with saved Smart Components, opens the Smart Feature Insert PropertyManager page; in the FeatureManager design tree, **History >** *Smart\_Component\_name* > **Smart Feature RMB menu > Insert** |
| **swCommands\_Insert\_Stock\_Net** | 2176; valid for parts with a selected sketch; **Features toolbar > Boundary Boss/Base** |
| **swCommands\_Insert\_Target\_Point** | 1044; valid for a selected drawing view, activates the point cursor; after calling this command, select the location where to insert a datum target point |
| **swCommands\_Insert\_Walkthrough** | 2960; **View toolbar > Add Walk-through** or **View menu > Lights and Cameras > Add Walk-through** or **Large Design Review tab > Add Walk-through** |
| **swCommands\_Insert\_Weld** | 1024; valid for assemblies, opens the Weld Bead Type dialog |
| **swCommands\_Insert\_Zone** | 1139; valid for assemblies, opens an Open dialog with which to select the component to insert as an envelope feature |
| **swCommands\_InsertAbbrView** | 3466; Opens the Model Break View PropertyManager; **Insert > Model Break View...** |
| **swCommands\_InsertAutoDim** | 3244; valid for a selected sketch, applies the correct dimension based on selected entities; **Dimension/Relations toolbar > Auto Insert Dimension** |
| **swCommands\_InsertBelt** | 616; valid for assemblies, opens the Belt/Chain PropertyManager page; **Assembly** or **Blocks toolbar > Belt/Chain** |
| **swCommands\_InsertBends** | 118; valid for sheet metal parts; **Sheet Metal toolbar > Insert Bends** |
| **swCommands\_InsertBlock** | 470; valid for a selected plane or planar face, opens the Insert Block PropertyManager page; **Layout Tools** or **Blocks toolbar > Insert Block** |
| **swCommands\_InsertBoundarySurface** | 618; valid for parts, opens a Boundary-Surface PropertyManager page; **Surfaces toolbar > Boundary Surface** or **Insert menu > Surface > Boundary Surface** |
| **swCommands\_InsertCenterOfMass** | 3057; valid for parts with a selected sketch; **Features toolbar > Reference Geometry > Center of Mass** or **Reference Geometry toolbar > Center of Mass** |
| **swCommands\_InsertCenterOfMassRefPoint** | 3069; valid for parts with a Center of Mass; in the graphics area, c*enter\_of\_mass* **context toolbar > Center of Mass Reference Point** |
| **swCommands\_InsertComponents** | 13; valid for assemblies, opens the Insert Component PropertyManager page; **Assembly toolbar > Insert Component** |
| **swCommands\_InsertCV** | 3100; valid for open style splines; **Spline Tools toolbar > Insert Control Vertex** |
| **swCommands\_InsertDetailCenterLine** | 425; valid for drawings, opens the Centerline PropertyManager page; **Annotation toolbar > Centerline** |
| **swCommands\_InsertDrawingviewSection** | 34; valid for a selected drawing view; **Drawing toolbar > SectionView** |
| **swCommands\_InsertFaceDraft** | 40; valid for parts with a selected sketch; **Features toolbar > Draft** |
| **swCommands\_InsertFamilyTable** | 410; **Insert menu > Tables > Family T**able or **Tables toolbar > Family Table** |
| **swCommands\_InsertFamilyTable\_Drw** | 3537; **Insert menu > Tables > Family T**able or **Tables toolbar > Family Table** |
| **swCommands\_InsertFeatureBlend** | 322; for assemblies with a mold base and design parts; **Mold Tools toolbar > Filled Surface** |
| **swCommands\_InsertFeatureMoveFace** | 538; valid for parts, opens the Move Face ProeprtyManager page; **Features toolbar > Move Face** |
| **swCommands\_InsertFeatureNudge** | 2928; valid for assemblies with a mold base and design parts; **Mold Tools toolbar > Move Face** |
| **swCommands\_InsertHandSketch** | 3243; valid for systems supporting stylus/pen hardware, inserts a pen sketch; **Sketch toolbar > Pen Sketch** |
| **swCommands\_InsertHyperlink** | 134; opens an Insert Hyperlink dialog; **Web toolbar > Insert Hyperlink** |
| **swCommands\_InsertLiveSection** | 2843; valid for parts and a selected face; **Features toolbar > Live Section Plane** |
| **swCommands\_InsertMoldFolders** | 546; valid for parts; **Mold Tools toolbar > Insert Mold Folders** |
| **swCommands\_InsertNewFamilyMember** | 3452; 3DEXPERIENCE SOLIDWORKS only, for a selected family member in ConfigurationManager, launches an Add Family Member PropertyManager to add a new part/assembly family member; **ConfigurationManager >** *family\_member* **RMB menu > New Family Member** |
| **swCommands\_InsertNewPrivateFamilyMember** | 3454; 3DEXPERIENCE SOLIDWORKS only, for a selected family member in ConfigurationManager, launches an Add Family Member PropertyManager to add a new private part/assembly family member that cannot be saved in the platform as a physical product; **ConfigurationManager >** *family\_member* **RMB menu > New Family Member** |
| **swCommands\_InsertNewRepresentation** | 3453; 3DEXPERIENCE SOLIDWORKS only, for a selected family member in ConfigurationManager, launches an Add Representation PropertyManager to add a new part/assembly representation of the configuration which is not managed on the platform as a physical product but has the same part number as the family member to which it is associated; **ConfigurationManager >** *family\_member* **RMB menu > New Family Member** |
| **swCommands\_InsertOffsetRefSurface** | 105; valid for assemblies with a mold base and design parts; **Mold Tools toolbar > Offset Surface** |
| **swCommands\_InsertPart** | 26; valid for parts, opens the Open dialog; **Features toolbar > Insert Part** |
| **swCommands\_InsertPartingLine** | 111; valid for assemblies with a mold base and design parts; **Mold Tools toolbar > Split Line** or **Feature toolbar > Curves > Split Line** |
| **swCommands\_InsertPartingPlane** | 449; valid for parts; **Mold Tools toolbar > Parting Surfaces** |
| **swCommands\_InsertPlanarSurface** | 168; valid for parts, opens the Planar Surface PropertyManager page; **Surfaces** or **Mold Tools toolbar > Planar Surface** |
| **swCommands\_InsertPlane** | 23; valid for parts with a selected sketch; **Features toolbar > Reference Geometry > Plane** |
| **swCommands\_InsertRefpoint** | 455; valid for parts with a selected sketch; **Features toolbar > Reference Geometry > Point** or **Reference Geometry toolbar > Point** |
| **swCommands\_InsertRefsurfaceRadiate** | 155; valid for assemblies with a mold base and design parts; **Mold Tools toolbar > Radiate Surface** |
| **swCommands\_InsertRefsurfaceSew** | 156; valid for assemblies with a mold base and design parts; **Mold Tools toolbar > Knit Surface** |
| **swCommands\_InsertRuledSurfaceFromEdge** | 448; valid for assemblies with a mold base and design parts; **Mold Tools toolbar > Ruled Surface** |
| **swCommands\_InsertScale** | 350; valid for assemblies with a mold base and design parts; **Mold Tools toolbar > Scale** |
| **swCommands\_InsertSketchBelt** | 611; valid for sketches with circles or arcs; **Blocks toolbar > Belt/Chain** |
| **swCommands\_InsertSketchEQCurve** | 2881; valid for open sketches; **Sketch toolbar > Equation Driven Curve** |
| **swCommands\_InsertSplinePoint** | 140; valid for an open sketch of a spline; **Spline Tools toolbar > Insert Spline Point** |
| **swCommands\_InsertSplitFeat** | 397; valid for a selected solid body in a part; **Features toolbar > Split** |
| **swCommands\_InsertStructConnection** | 3445; **Structure System toolbar > Insert structural connection element** |
| **swCommands\_InsertStudWiz** | 3489; **Insert menu > Features > Stud Wizard**...; Inserts a stud using a pre-defined cross-section |
| **swCommands\_InsertSubdExtrude** | 3328; **Insert menu > Freeshape > Extrude** |
| **swCommands\_InsertSubdRevolve** | 3329; **Insert menu > Freeshape > Revolve** |
| **swCommands\_InsertSubdSweep** | 3330; **Insert menu > Freeshape > Sweep** |
| **swCommands\_InsertSymmDiaDim** | 3490; **Tools menu > Dimensions > Symmetric**; Creates a reference diameter dimension between selected entities |
| **swCommands\_InsertThreadWiz** | 3181; valid for parts with a selected sketch; **Features toolbar > Thread** |
| **swCommands\_Int\_Tree\_Ignore** | 2613; valid in an open Interference Detection DVE after calculation; **Interference Detection PropertyManager page > Results >** *interference\_tree* **RMB menu > Ignore** |
| **swCommands\_Int\_Tree\_Open** | 2614; valid in an open Interference Detection DVE after calculation; **Interference Detection PropertyManager page > Results >** *interference\_tree* **RMB menu > Open** |
| **swCommands\_Int\_Tree\_Unignore** | 2615; valid in an open Interference Detection DVE after calculation and only if **Interference Detection > Options > Show ignored interferences** is selected; **Interference Detection PropertyManager page > Results >** *interference\_tree* **RMB menu > Unignore** |
| **swCommands\_Int\_Tree\_Zoom** | 2616; valid in an open Interference Detection DVE after calculation; **Interference Detection PropertyManager page > Results >** *interference\_tree* **RMB menu > Zoom to selection** |
| **swCommands\_InterferenceDetection** | 344; valid for assemblies; **Assembly toolbar > Interference Detection** |
| **swCommands\_Internal\_Dimension** | 2594; valid for a selected dimension, toggles the Internal Dimension state and rebuilds the browser tree |
| **swCommands\_IntersectionCurve** | 306; valid for sketches; **Sketch toolbar > Intersection Curve** |
| **swCommands\_IntersectionSnap** | 524; valid for sketches; **Quick Snaps toolbar > Intersection Snap** |
| **swCommands\_InvertSelection** | 564; **Selection Filter toolbar > Invert Selection** |
| **swCommands\_Iso\_Draw\_Electrical\_Rt** | 3353; **Tools menu > Routing > Electrical > Create Drawing** |
| **swCommands\_Iso\_draw\_pipe\_rt** | 2948; valid for the SOLIDWORKS Routing add-in and an open piping assembly; Piping **toolbar > Pipe Drawing** |
| **swCommands\_Isolate\_Changed\_Dims** | 3023; valid for drawings saved in 2012 or later; **Dimensions/Relations toolbar > Isolate Changed Dimensions** |
| **swCommands\_Isometric** | 167; **View toolbar > View Orientation > Isometric** |
| **swCommands\_Italic** | 148; valid for selected text; **Formatting toolbar > Italic** |
| **swCommands\_Jog** | 372; valid for sheet metal parts; **Sheet Metal toolbar > Jog** |
| **swCommands\_Jog\_Ordinate** | 1518; valid for a drawing of a circle or arc with a selected angular running dimension; in the graphics area, *angular\_running\_dimensi*on **RMB menu > Display Options > Jog** |
| **swCommands\_JogLine** | 398; valid for a part with an open sketch and a selected segment; also valid for SOLIDWORKS Routing Add-in and an open route; **Explode Sketch toolbar > Jog Line** |
| **swCommands\_Join** | 116; valid for an assembly to which a new join part is being added; **Features toolbar > Join** (see the SOLIDWORKS help) |
| **swCommands\_Join\_Contours** | 2516; valid for contour or loft DVEs; *selection\_list\_box* **RMB menu  > Join Contours** |
| **swCommands\_Keep\_Constraints** | 2788; Move Confirm dialog resource **Keep** or **Dangle** |
| **swCommands\_Large\_Icon** | 1622; valid for content or palette list controls or component list views, **RMB menu > Large Icons** |
| **swCommands\_Large\_List\_Icon** | 2065; valid for content or palette list controls or component list views, **RMB menu > Large List Icons** |
| **swCommands\_LargeAssemblyMode** | 405; valid for assemblies; **Assembly toolbar > Large Assembly Mode** |
| **swCommands\_LaunchFilePrep\_Asst** | 3513; launches the File Preparation Assistant; **Tools menu > File Preparation Assistant...** |
| **swCommands\_Layer\_Select** | 1151; valid for drawings; **Layer toolbar > drop-down menu** |
| **swCommands\_Layer\_Toolbar** | 1955; alternative to swCommands\_Toolbar\_Layer; **View menu > Toolbars > Layer** |
| **swCommands\_LayerProperties** | 296; valid for drawings; **Line Format toolbar > Layer Properties** |
| **swCommands\_Layout** | 2817; alternative to swCommands\_Toolbar\_Layout; **View menu > Toolbars > Layout Tools** |
| **swCommands\_LayoutDefault** | 2888; **View menu > Workspace > Default** |
| **swCommands\_LayoutDualMonitor** | 2890; **View menu > Workspace > Dual Monitor** |
| **swCommands\_LayoutWidescreen** | 2889; **View menu > Workspace > Widescreen** |
| **swCommands\_LDR\_Update\_Model\_Graphics** | 3090; valid for a selected assembly opened in Large Design Review mode; in the FeatureManager design tree, *top\_level\_assembly* **RMB menu > Update Model Graphics** |
| **swCommands\_Leader\_Add\_Bent** | 1780; valid for a drawing view with a selected leader; in the graphics area, *leader* **RMB menu > Add Jog Point** |
| **swCommands\_Leader\_Add\_Branch** | 1778; valid for a drawing view with a selected leader; in the graphics area, *leader* **RMB menu > Insert New Branch** |
| **swCommands\_Leader\_Delete\_All** | 1781; valid for a drawing with a selected multi-jog leader; in the graphics area, *multi\_jog\_leader* **RMB menu > Delete Leader** |
| **swCommands\_Leader\_Delete\_Bent** | 1779; valid for a drawing view with a selected leader that has a jog; in the graphics area, *leader* **RMB menu > Delete Jog Point** |
| **swCommands\_Leader\_Delete\_Branch** | 722; valid for a drawing view with a selected leader that has a branch; in the graphics area, *leader* **RMB menu > Delete Branch** |
| **swCommands\_Left** | 164; **View menu > View Orientation > Left** |
| **swCommands\_LengthSnap** | 540; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; **Quick Snaps toolbar > Length Snap** |
| **swCommands\_Light\_Properties** | 1296; valid for a selected SOLIDWORKS Light in the FeatureManager design tree if **Scene, Lights, and Cameras > SOLIDWORKS Lights RMB menu > Show Lights** is selected; in the graphics area, *light* **RMB menu > Properties**; valid for a selected camera in DisplayManager; **Camera >** *Camera1* **RMB menu > Edit Camera** |
| **swCommands\_Lightweight\_All** | 1235 valid for a selected assembly with resolved components; in the FeatureManager design tree, *top\_level\_assy* **RMB menu > Set Resolved to Lightweight** |
| **swCommands\_Line** | 43; valid for an open sketch; **Layout Tools** or **Sketch toolbar > Line** |
| **swCommands\_Line\_Center** | 1312; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Style > Center** |
| **swCommands\_Line\_Chain** | 1311; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Style > Chain** |
| **swCommands\_Line\_Dashed** | 1309; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Style > Dashed** |
| **swCommands\_Line\_Normal** | 1317; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Thickness > 0.25mm** |
| **swCommands\_Line\_Phantom** | 1310; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Style > Phantom** |
| **swCommands\_Line\_Solid** | 1308; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Style > Solid** |
| **swCommands\_Line\_Stitch** | 1313; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Style > Stitch** |
| **swCommands\_Line\_Stylebylayer** | 1307; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Style > Default** |
| **swCommands\_Line\_Thick** | 1318; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Thickness > 0.35mm** |
| **swCommands\_Line\_Thick2** | 1319; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Thickness > 0.5mm** |
| **swCommands\_Line\_Thick3** | 1320; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Thickness > 0.7mm** |
| **swCommands\_Line\_Thick4** | 1321; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Thickness > 1mm** |
| **swCommands\_Line\_Thick5** | 1322; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Thickness > 1.4mm** |
| **swCommands\_Line\_Thick6** | 1323; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Thickness > 2mm** |
| **swCommands\_Line\_Thickthin** | 1314; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Style > Thin/Thick Chain** |
| **swCommands\_Line\_Thin** | 1316; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Thickness > 0.18mm** |
| **swCommands\_Line\_Weightbylayer** | 1315; valid for drawings with a selected line; in the graphics area, *selected\_edge* **RMB context toolbar > Line Thickness > Default** |
| **swCommands\_LinearMotor** | 422; valid for MotionManager, opens the Motor PropertyManager page; **MotionManager toolbar > Motor** |
| **swCommands\_LinearPattern** | 18; valid for parts with a selected sketch; **Features toolbar > Linear Pattern** |
| **swCommands\_LinearSketchPattern** | 172; valid for an open sketch; **Sketch toolbar > Linear Sketch Pattern** |
| **swCommands\_LinearSpring** | 444; valid for MotionManager, opens the Motor PropertyManager page; **MotionManager toolbar > Spring** |
| **swCommands\_LineColor** | 141; valid for drawings and selected sketches; **Line Format toolbar > Line Color** |
| **swCommands\_LineFormats** | 481; alternative to swCommands\_Toolbar\_Lineformat; **View menu > Toolbars > Line Format** |
| **swCommands\_LineStyle** | 143; valid for drawings and selected sketches; **Line Format toolbar > Line Style** |
| **swCommands\_LineThickness** | 142; valid for drawings and selected sketches; **Line Format toolbar > Line Thickness** |
| **swCommands\_Link\_Dims** | 1543; valid for sketches with dimensions, opens the Shared Values dialog; in the graphics area, *dimension* **RMB menu > Link Values** |
| **swCommands\_LinkViews** | 553; valid for two or more viewport views; **Standard Views toolbar > Link Views** or **Window menu > Viewport > Link Views** |
| **swCommands\_List\_Body\_References** | 2803; valid for a selected body in a part, opens the References for *body* dialog |
| **swCommands\_List\_Comp\_References** | 2802; valid for a selected component in an assembly, opens the References for *comp* dialog |
| **swCommands\_List\_Edge\_References** | 2806; valid for a selected edge in a part, opens the References for Edge dialog |
| **swCommands\_List\_Exportents** | 1080; valid for parts with named entities, opens the Named Entities dialog; in the FeatureManager design tree, *top\_level\_part* **RMB menu > List Named Entities** |
| **swCommands\_List\_Extrefs** | 1055; valid for parts and assemblies with external references, opens the External References For dialog; **FeatureManager design tree >** *Assembly* **RMB menu > List External Refs** |
| **swCommands\_List\_Face\_References** | 2805; valid for a selected face in a part, opens the References for Face dialog |
| **swCommands\_List\_Feat\_References** | 2804; valid for a selected feature in a part, opens the References for *feat* dialog |
| **swCommands\_List\_Vert\_References** | 2807; valid for a selected vertex in a part, opens the References for Vertex dialog |
| **swCommands\_LiveSectionFitToPart** | 2844; valid for models with a live section plane; in the graphics area, *live\_section\_plane* **RMB menu > Fit To Part** |
| **swCommands\_LiveSectionReset** | 2845; valid for models with a live section plane; in the graphics area, *live\_section\_plane* **RMB menu > Reset** |
| **swCommands\_LiveSectionTriadHide** | 2847; valid for models with a live section plane; in the graphics area, *live\_section\_plane* **RMB context toolbar > Show Triad** |
| **swCommands\_LiveSectionTriadShow** | 2846; valid for models with a live section plane; in the graphics area, *live\_section\_plane* **RMB context toolbar > Hide Triad** |
| **swCommands\_Lock\_Bom** | 918; valid for a drawing view with an Excel-based Bill of Materials; in the graphics area, *BOM\_table* **RMB menu > Anchor > Lock to Anchor** |
| **swCommands\_Lock\_Configuration** | 1847; valid in a PDM-enabled environment with an unlocked configuration; in ConfigurationManager, *unlocked\_config* **RMB menu > Lock Configuration** |
| **swCommands\_Lock\_Unlock\_Focus** | 2617; valid for drawings; in the graphics area or the FeatureManager design tree, *drawing\_view* **RMB menu > Lock View Focus** or **Unlock View Focus** |
| **swCommands\_Lock\_Unlock\_Focus\_Double\_Click** | 2618; valid for drawings; in the graphics area or the FeatureManager design tree, *drawing\_view* **RMB menu >** *double click* |
| **swCommands\_LockViewPlane** | 3436; valid for assemblies displaying a section view; **graphics area RMB > Lock View** |
| **swCommands\_LoftedBend** | 406; valid for sheet metal parts; **Sheet Metal toolbar > Lofted-Bend** |
| **swCommands\_LoftedBossBase** | 25; valid for parts with a selected sketch; **Features toolbar > Lofted Boss/Base** |
| **swCommands\_LoftedCut** | 82; valid for parts with a selected sketch; **Features toolbar > Lofted Cut** |
| **swCommands\_LoftedSurface** | 107; valid for parts; **Surfaces toolbar > Lofted Surface** |
| **swCommands\_LoopDve** | 3098; valid for a selected plane, planar face, or edge on a part, opens the Path PropertyManager page |
| **swCommands\_Machined\_Parts\_Costing** | 3028; **SOLIDWORKS Costing task pane > Machining Costing** |
| **swCommands\_Macros** | 482; alternative to swCommands\_Toolbar\_Macro; **View menu > Toolbars > Macro** |
| **swCommands\_MagnetLine** | 3007; valid for drawings with a selected start point for a magnetic line with which to align balloons; **Annotation toolbar > Magnetic Line** |
| **swCommands\_Make\_Edit\_Sketch** | 3419; converts the selected reference sketch to an edit sketch; **RMB menu > Make Edit Sketch** |
| **swCommands\_Make\_Lightweight** | 1202; valid for assemblies with a resolved component; in the FeatureManager design tree, *resolved\_component* **RMB menu > Set to Lightweight** |
| **swCommands\_Make\_Reference\_Sketch** | 3420; converts the selected edit sketch to a reference sketch; **RMB menu > Make Reference Sketch** |
| **swCommands\_Make\_Resolved** | 1203; valid for assemblies with a lightweight component; in the FeatureManager design tree, *lightweight\_component* **RMB menu > Set to Resolved** |
| **swCommands\_Make\_Suppressed** | 1204; valid for one or more selected components in an assembly |
| **swCommands\_Make\_Trim\_As\_Construction** | 3331; valid when the Trim PropertyManager is active, **graphics area RMB menu > Keep trimmed entities as construction geometry** |
| **swCommands\_MakeAssemblyFromPartAssembly** | 462; opens the Begin Assembly PropertyManager page; **Standard toolbar > Make Assembly From Part/Assembly** |
| **swCommands\_MakeBlock** | 469; **Blocks toolbar > Make Block** |
| **swCommands\_MakeDrawingFromPartAssembly** | 461; opens the Sheet Format/Size dialog to create a drawing; **Standard toolbar > Make Drawing from Part/Assembly** |
| **swCommands\_MakeSmartComponent** | 563; valid for assemblies, opens the Smart Component PropertyManager page; **Assembly toolbar > Make Smart Component** |
| **swCommands\_MakeVirtualCompIndependent** | 3494; Makes the selected virtual assembly component independent; in the FeatureManager design tree, right-click a virtual assembly component and select **Make Independent** |
| **swCommands\_Manage\_Equations** | 3040; opens the Equations, Global Variables, and Dimensions dialog; in the FeatureManager design tree, **Equations RMB menu > Manage Equations** |
| **swCommands\_Manual\_Viewlabel** | 2073; valid for drawings with a selected view location label; in the graphics area, *location\_label* **RMB menu > Manual View Label Text** |
| **swCommands\_Mark\_LDR\_Config** | 3204; valid for an assembly opened in Resolved or Lightweight mode, allows the user to mark the configurations to display when the assembly is opened in Large Design Review mode; in the ConfigurationManager, *top\_level\_assembly* **RMB menu > Large Design Review Mark menu** |
| **swCommands\_Mark\_LDR\_ConfigActive** | 3206; valid for an assembly opened in Resolved or Lightweight mode, allows the user to mark the active configuration for display when the assembly is opened in Large Design Review mode; in the ConfigurationManager, *top\_level\_assembly* **RMB menu > Large Design Review Mark** **> Add Large Design Review Mark for This Configuration** |
| **swCommands\_Mark\_LDR\_ConfigAll** | 3207; valid for an assembly opened in Resolved or Lightweight mode, allows the user to mark all of the configurations for display when the assembly is opened in Large Design Review mode; in the ConfigurationManager, *top\_level\_assembly* **RMB menu > Large Design Review Mark > Add Large Design Review Mark for All Configurations** |
| **swCommands\_Mark\_LDR\_ConfigOff** | 3205; valid for an assembly opened in Resolved or Lightweight mode, allows the user to unmark a configuration to prevent its display when the assembly is opened in Large Design Review mode; in the ConfigurationManager, *top\_level\_assembly* **RMB menu > Large Design Review Mark > Remove Large Design Review Mark** |
| **swCommands\_Mark\_LDR\_ConfigSpecific** | 3208; valid for an assembly opened in Resolved or Lightweight mode, allows the user to mark a specific configuration to display when the assembly is opened in Large Design Review mode; in the ConfigurationManager, *top\_level\_assembly* **RMB menu > Large Design Review Mark > Add Large Design Review Mark for Specified Configurations** |
| **swCommands\_Mark\_Smart\_Fastener\_Uptodate** | 2464; valid only for Toolbox add-ins and an assembly with a selected Smart Fastener; in FeatureManager design tree, *smart\_fastener\_feature* **RMB menu > Mark up to date** |
| **swCommands\_Mark\_Smart\_Insert\_Uptodate** | 1857; valid only for Toolbox add-ins and an assembly with a Smart Insert that needs to be updated; in the graphics area, **RMB menu > Update Smart Insert** |
| **swCommands\_MassProperties** | 343; **Tools toolbar > Mass Properties** |
| **swCommands\_Mate** | 90; valid for assemblies with two or more selected components to mate; **Assembly toolbar > Mate** |
| **swCommands\_Mate\_Cancel** | 698; Add Mate dialog resource **Undo** |
| **swCommands\_Mate\_Delete** | 2517; valid in the assembly Mate PropertyManager page for a selected mate; **Mates tab > Mate Selections >** *mate* **RMB menu > Delete** |
| **swCommands\_Mate\_Preview** | 702; Add Mate dialog resource **Preview** |
| **swCommands\_MateReference** | 160; valid for parts with a selected sketch; **Features toolbar > Reference Geometry > Mate Reference** or **Reference Geometry toolbar > Mate Reference** |
| **swCommands\_Mating\_Component** | 3305; applies dimensions and tolerances on target based on source component; **DimXpert toolbar > Auto Pair Tolerance** |
| **swCommands\_MBD** | 3140; **View menu > Toolbars > SOLIDWORKS MBD** |
| **swCommands\_MBD\_Load\_Unload** | 3185; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS MBD SNL** |
| **swCommands\_MBD\_Template\_Editor** | 3142; **SOLIDWORKS MBD toolbar > 3D PDF Template Editor** |
| **swCommands\_Measure** | 92; opens the Measure dialog; **Tools toolbar > Measure** |
| **swCommands\_Measure\_Csys** | 2104; **Measure dialog > XYZ Relative To** |
| **swCommands\_Measure\_History** | 3066; **Measure dialog > Measurement History** |
| **swCommands\_Measure\_Minmax** | 2101; valid for the Measure dialog if Point-to-Point is not selected; **Measure dialog > Arc/Circle Measurements** |
| **swCommands\_Measure\_Proj** | 2100; **Measure dialog > Projected On** |
| **swCommands\_Measure\_Proj\_None** | 2108; valid for the Measure dialog; **Projected On > None** |
| **swCommands\_Measure\_Proj\_Plane** | 2110; valid for the Measure dialog; **Projected On > Select Face/Plane** |
| **swCommands\_Measure\_Proj\_Recent** | 2111; valid for the Measure dialog; **Projected On >** *no selection* |
| **swCommands\_Measure\_Proj\_Screen** | 2109; valid for the Measure dialog; **Projected On > Screen** |
| **swCommands\_Measure\_PtoP** | 3065; **Measure dialog > Point-to-Point** |
| **swCommands\_Measure\_Showcallouts** | 2398; valid if **Measure dialog > Show XYZ Measurements** is selected and an entity is selected; in the graphics area, *measurement callout* **RMB menu > Show XYZ dimensions and associated geometry** |
| **swCommands\_Measure\_Units** | 2102; opens the Measure Units/Precision dialog; **Measure dialog > Units/Precision** |
| **swCommands\_Measure\_Xyz** | 2103; **Measure dialog > Show XYZ Measurements** |
| **swCommands\_Midpointline** | 3118; **Sketch toolbar > Midpoint Line** |
| **swCommands\_MidpointSnap** | 523; valid for sketches; **Quick Snaps toolbar > Midpoint Snap** |
| **swCommands\_MidSurface** | 117; valid for parts with offset face pairs, opens the MidSurface1 PropertyManager page; **Surfaces toolbar > Mid-Surface** |
| **swCommands\_Mirrcmd\_Browse** | 1687; valid if the Mirror Components PropertyManager page is open, opens the Choose File dialog; **Mirror Components > Step 3: Opposite Hand > Opposite Hand Versions > Create new files >** *browse\_button* |
| **swCommands\_Mirrcmd\_Copy\_All\_Instances** | 1686; valid for a selected subassembly and an open Mirror Components PropertyManager page; **Mirror Components > Step 2: Set Orientation > Orient Components >** *top\_level\_comp* **RMB menu > Copy All Instances** |
| **swCommands\_Mirrcmd\_Mirror\_All\_Children** | 1683; valid for a selected subassembly and an open Mirror Components PropertyManager page; **Mirror Components > Step 2: Set Orientation > Orient Components >** *top\_level\_comp* **RMB menu > Mirror All Children** |
| **swCommands\_Mirrcmd\_Mirror\_All\_Instances** | 1684; valid for a selected subassembly and an open Mirror Components PropertyManager page; **Mirror Components > Step 2: Set Orientation > Orient Components >** *top\_level\_comp* **RMB menu > Mirror All Instances** |
| **swCommands\_Mirror** | 83; valid for parts with a selected sketch; **Features toolbar > Mirror** or for assemblies with a selected assembly feature, opens the Mirror PropertyManager page**; Insert > Assembly Feature > Mirror** |
| **swCommands\_MirrorEntities** | 61; valid for an open sketch, opens the Mirror PropertyManager page; **Sketch** or **Layout Tools toolbar > Mirror Entities** |
| **swCommands\_MiterFlange** | 324; valid for sheet metal parts; **Sheet Metal toolbar > Miter Flange** |
| **swCommands\_MixModel\_LightWeight** | 3322; **Assembly toolbar > Set Component to Lightweight** |
| **swCommands\_MixModel\_Resolve** | 3321; **Assembly toolbar > Set Component to Resolved** |
| **swCommands\_ModelItems** | 513; valid for drawings; **Annotation toolbar > Model Items** |
| **swCommands\_ModelView** | 77; valid for drawings, opens the Model View PropertyManager page; **Drawing toolbar > Model View** |
| **swCommands\_Modify\_Curv\_Scale** | 646; valid for a selected curve with curvature combs, opens the Curvature Scale PropertyManager page; in the graphics area, *curve* **RMB menu > Modify Curvature Scale** |
| **swCommands\_ModifySketch** | 100; valid for selected sketches, opens the Modify Sketch dialog; **Sketch toolbar > Modify Sketch** |
| **swCommands\_MoldflowxpressAnalysisWizard** | 414; runs the MoldflowXpress Analysis Wizard, if the product is available |
| **swCommands\_Molds** | 483; alternative to swCommands\_Toolbar\_Mold; **View menu > Toolbars > Mold Tools** |
| **swCommands\_MostRecentlyUsed\_File1** | 3365; opens file 1 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File10** | 3374; opens file 10 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File11** | 3375; opens file 11 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File12** | 3376; opens file 12 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File13** | 3377; opens file 13 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File14** | 3378; opens file 14 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File15** | 3379; opens file 15 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File16** | 3380; opens file 16 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File2** | 3366; opens file 2 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File3** | 3367; opens file 3 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File4** | 3368; opens file 4 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File5** | 3369; opens file 5 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File6** | 3370; opens file 6 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File7** | 3371; opens file 7 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File8** | 3372; opens file 8 in **File > Open Recent** |
| **swCommands\_MostRecentlyUsed\_File9** | 3373; opens file 9 in **File > Open Recent** |
| **swCommands\_Move\_Down\_Using\_Arrow\_Key** | 2001; VK\_DOWN; shift-control-down arrow key |
| **swCommands\_Move\_Dve\_Resume\_Drag** | 1464; valid for collision detection and dynamic clearance list boxes in the Move Component PropertyManager page; **RMB menu > Resume Drag** |
| **swCommands\_Move\_Left\_Using\_Arrow\_Key** | 2002; VK\_LEFT; shift-control-left arrow key |
| **swCommands\_Move\_Right\_Using\_Arrow\_Key** | 2003; VK\_RIGHT; shift-control-left arrow key |
| **swCommands\_Move\_Show\_Delta\_Xyz** | 1135; valid after *component* **RMB menu > Move with Triad** command in an assembly; in the graphics area, *triad\_center\_ball* **RMB menu > Show Translate Delta XYZ Box** |
| **swCommands\_Move\_Show\_Xyz** | 1142; valid after *component* **RMB menu > Move with Triad** command in an assembly; in the graphics area, *triad\_center\_ball* **RMB menu > Show Translate XYZ Box** |
| **swCommands\_Move\_Up\_Using\_Arrow\_Key** | 2000; VK\_UP; shift-control-up arrow key |
| **swCommands\_MoveComponent** | 20; valid for assemblies, opens the Move Component PropertyManager page; in the graphics area, **RMB menu > Move Component** |
| **swCommands\_MoveCopyBodies** | 408; valid for multibody parts; **Features toolbar >** **Move/Copy Bodies** |
| **swCommands\_MoveEntities** | 502; valid for an open sketch, opens the Move PropertyManager page; **Sketch toolbar > Move Entities** |
| **swCommands\_MoveSizeFeatures** | 386; valid for parts; **Features toolbar > Instant3D** |
| **swCommands\_MultiJogLeader** | 367; valid for drawings; **Annotation toolbar > Multi-jog Leader** |
| **swCommands\_Near\_Stack\_Smart\_Fastener** | 2454; valid for a Smart Hole Fastener in an assembly; *smart\_hole\_fastener\_tree\_item* **RMB > Top stack** |
| **swCommands\_NearestSnap** | 520; valid for sketches; **Quick Snaps toolbar > Nearest Snap** |
| **swCommands\_New** | 1; **File menu > New**; **Standard toolbar > New** |
| **swCommands\_New\_Display\_State** | 2129; **Visual Overlay dialog toolbar > New Display State** |
| **swCommands\_New\_Subassembly** | 1258; valid for assemblies; in the FeatureManager design tree, *top\_level\_assembly* **RMB menu > Insert New Subassembly** |
| **swCommands\_New\_Toolbar\_Sel\_Filter** | 1177; alternative to swCommands\_SelectionFilters; **View menu > Toolbars > Selection Filter** |
| **swCommands\_New\_View** | 1231; opens a Named View dialog; **View toolbar > View Orientation > New View** |
| **swCommands\_NewAssembly** | 295; valid for assemblies; **Assembly toolbar > New Assembly** |
| **swCommands\_NewMacro** | 573; opens the Save As dialog; **Macro toolbar > New Macro** |
| **swCommands\_NewMacroButton** | 272; creates custom macros, swCommands\_UserMacro01 - swCommands\_UserMacro98; **Macro toolbar > New Macro Button** |
| **swCommands\_NewPart** | 91; valid for assemblies with a selected face or plane; **Assembly toolbar > New Part** |
| **swCommands\_NewWindow** | 580; **Window menu > New Window**; **Standard toolbar > New Window** |
| **swCommands\_NextCmdMgrTab** | 3046; navigates to the next CommandManager tab |
| **swCommands\_NoBends** | 139; valid for sheet metal parts; **Sheet Metal toolbar > No Bends** |
| **swCommands\_NoCommand** | -3; no command is running |
| **swCommands\_NoExternalReferences** | 578; valid for assemblies; **Assembly toolbar > No External References** |
| **swCommands\_NormalTo** | 169; **View toolbar > View Orientation > Normal To** |
| **swCommands\_NoSolveMove** | 171; valid for parts; **Sketch toolbar > No Solve Move** |
| **swCommands\_Note** | 36; opens the Note PropertyManager page; **Annotation toolbar > Note** |
| **swCommands\_NoteCPat** | 2994; opens the Circular Note Pattern PropertyManager page; **Annotation toolbar > Circular Note Pattern** |
| **swCommands\_NoteLPat** | 2993; opens the LinearNote Pattern PropertyManager page; **Annotation toolbar > Linear Note Pattern** |
| **swCommands\_Number** | 539; valid for selected text; **Formatting toolbar > Number** |
| **swCommands\_Numeric\_Input\_Toggle** | 3029; **Sketch toolbar > Sketch Numeric Input** |
| **swCommands\_Nx\_Rmb\_Auto\_Ok** | 2744; valid if SelectionManager is open; in the graphics area, **RMB menu > Auto-OK Selections** |
| **swCommands\_Nx\_Rmb\_Cancel** | 2736; valid if SelectionManager is open; in the graphics area, **RMB menu > Cancel** |
| **swCommands\_Nx\_Rmb\_Clear\_All** | 2737; valid if SelectionManager is open with multiple selections; in the graphics area, **RMB menu > Clear All** |
| **swCommands\_Nx\_Rmb\_Ok** | 2735; valid if SelectionManager is open and with multiple selections; in the graphics area, **RMB menu > OK** |
| **swCommands\_Nx\_Rmb\_Push\_Pin** | 2743; valid if SelectionManager is open; in the graphics area, **RMB menu > Pin Dialog** |
| **swCommands\_Nx\_Rmb\_Sel\_Closed\_Loop** | 2741; valid if SelectionManager is open; in the graphics area, **RMB menu > Select Closed Loop** |
| **swCommands\_Nx\_Rmb\_Sel\_Group** | 2739; valid if SelectionManager is open; in the graphics area, **RMB menu > Select Group** |
| **swCommands\_Nx\_Rmb\_Sel\_Open\_Loop** | 2740; valid if SelectionManager is open; in the graphics area, **RMB menu > Select Open Loop** |
| **swCommands\_Nx\_Rmb\_Sel\_Region** | 2742; valid if SelectionManager is open; in the graphics area, **RMB menu > Select Region** |
| **swCommands\_Nx\_Rmb\_Sel\_Regular** | 2738; valid if SelectionManager is open; in the graphics area, **RMB menu > Select** |
| **swCommands\_Nx\_Sel\_Clear\_All** | 2722; **SelectionManager dialog > Clear** |
| **swCommands\_Nx\_Sel\_Group** | 2721; **SelectionManager dialog > Select Group** |
| **swCommands\_Nx\_Sel\_Loop** | 2720; **SelectionManager dialog > Select Closed Loop** |
| **swCommands\_Nx\_Sel\_Open\_Loop** | 2723; **SelectionManager dialog > Select Open Loop** |
| **swCommands\_Nx\_Sel\_Region** | 2724; **SelectionManager dialog > Select Region** |
| **swCommands\_Nx\_Sel\_Regular** | 2725; **SelectionManager dialog > Standard Selection** |
| **swCommands\_Nx\_Select\_Manager** | 2718; opens the SelectionManager dialog which is valid only during creation of loft, sweep, and boundary surface features and path mates; in the graphics area, **RMB menu > SelectionManager** |
| **swCommands\_Nx\_Select\_Manager\_End** | 2719; valid if SelectionManager is open during creation of loft, sweep, and boundary surface features and path mates; in the active PropertyManager page list box, **RMB menu > End SelectionManager** |
| **swCommands\_Object\_Displayasicon** | 799; valid for an embedded OLE object; **Edit menu > Object > Display as Icon** |
| **swCommands\_Object\_Displaycontent** | 798; valid for an embedded OLE object; **Edit menu > Object > Display Content** |
| **swCommands\_Object\_Popup\_Menu** | 672; embedded OLE object popup menu |
| **swCommands\_Object\_Resetsize** | 800; valid for an embedded OLE object; **Edit menu > Object > Reset Size** |
| **swCommands\_OfficeAddin3dExperienceMarketPlace** | 3328; loads or unloads the 3DEXPERIENCE Marketplace add-in; **Standard toolbar > 3DEXPERIENCE Marketplace** |
| **swCommands\_OfficeButtonFlowSimulation** | 3146; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Flow Simulation** |
| **swCommands\_OfficeButtonInspection** | 3148; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Inspection** |
| **swCommands\_OfficeButtonPlastics** | 3147; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Plastics** |
| **swCommands\_OfficeButtonTolAnalyst** | 2894; **SOLIDWORKS Add-ins toolbar > TolAnalyst** |
| **swCommands\_Offset\_Dim\_Text** | 1607; valid for drawings with a selected dimension text; in the graphics area, *dimension\_text* **RMB menu > Display Options > Offset Text** |
| **swCommands\_OffsetEntities** | 76; valid for a selected face, edge, curve, or sketch entity in a part or assembly; **Layout Tools** or **Sketch toolbar > Offset Entities** |
| **swCommands\_OffsetOnSurface** | 3190; opens the Offset On Surface PropertyManager page; **Sketch toolbar > Offset On Surface** |
| **swCommands\_Ok** | 766; **OK** in dialogs |
| **swCommands\_Ok\_Command** | 3042; **Standard toolbar > OK** |
| **swCommands\_Ole\_Edit** | 1675; valid for a selected embedded OLE object; **RMB menu > Edit with** *tool\_name* |
| **swCommands\_Ole\_Property\_Sheet** | 1500; valid for a selected embedded OLE object, opens the OLE Object Property dialog; **RMB menu > Properties** |
| **swCommands\_On\_Demand\_Maufacturing** | 3499; Opens 3DEXPERIENCE Make in the SOLIDWORKS Task Pane. Make provides instant quotes for your parts and connects you with manufacturing service providers; only valid if 3DEXPERIENCE Marketplace Add-in is loaded and logged into; **Tools toolbar > On Demand Manufacturing** |
| **swCommands\_On\_Hide\_Cosmetic\_Welds** | 2998; valid for a weldment part with a visible weld bead feature and a selected Weld Folder; in the FeatureManager design tree, **Weld Folder RMB menu > Hide Cosmetic Welds** |
| **swCommands\_On\_Hold\_Cosmetic\_Welds\_Rebuild** | 3127; valid for a weldment part with a weld bead feature and a selected Weld Folder; in the FeatureManager design tree, **Weld Folder RMB menu > Suspend Automatic Rebuild** |
| **swCommands\_On\_Rebuild\_Cosmetic\_Welds** | 3128; valid for a weldment part with a weld bead feature and a selected Weld Folder; in the FeatureManager design tree, **Weld Folder RMB menu > Rebuild Welds** |
| **swCommands\_On\_Screen\_Dim\_Dialog** | 3488; For a selected drawing dimension, opens an on-screen dimension dialog that mirrors the Dimension Text section of the Dimension PropertyManager |
| **swCommands\_On\_Show\_Cosmetic\_Welds** | 2997; valid for a weldment part with a hidden weld bead feature and a selected Weld Folder; in the FeatureManager design tree, **Weld Folder RMB menu > Show Cosmetic Welds** |
| **swCommands\_Online\_Familytable\_Closed** | 3417 |
| **swCommands\_OnViewCenterOfMassSymbol** | 3059; **View toolbar > Hide/Show Items > View Center of Mass** |
| **swCommands\_Open** | 0; **File menu > Open;** **Standard toolbar > Open** |
| **swCommands\_Open\_Assembly** | 3009; valid for a drawing view with a selected assembly; in the FeatureManager design tree, *drw\_view\_assem* **RMB menu > Open Assembly** |
| **swCommands\_Open\_Associated\_Drw** | 2458; valid for a selected model, opens the Open dialog; in the FeatureManager design tree, *model* **RMB context toolbar > Open Drawing** |
| **swCommands\_Open\_Bookmark\_Editor** | 3515; valid only in SOLDWORKS Connected, accesses the Bookmark Editor; **Lifecycle and Collaboration toolbar > Add to Bookmark > Open Bookmark Editor** |
| **swCommands\_Open\_Comp\_Assem\_File** | 1377; valid for a selected component in a drawing, opens the component file |
| **swCommands\_Open\_Comp\_File** | 970; valid for a selected component in an assembly; in the FeatureManager design tree, *selected\_comp* **RMB context toolbar > Open Part** |
| **swCommands\_Open\_Detailing\_Drw** | 3497; opens drawing in detailing mode; **Standard toolbar > Open Drawing in Detailing Mode** |
| **swCommands\_Open\_LightWeight** | 3039; valid for assemblies opened in Large Design Review mode; **Assembly toolbar > Open in Lightweight** |
| **swCommands\_Open\_Part** | 3008; valid for a drawing view with a selected component; in the FeatureManager design tree, *drw\_view\_comp* **RMB toolbar > Open Part** |
| **swCommands\_Open\_Partdrawg\_For\_Drawing** | 3503; Opens the drawing for the selected part or assembly in the drawing; In a drawing view, **RMB on a part or assembly > Open Drawing** |
| **swCommands\_Open\_Sub\_Assembly** | 3011; valid for a drawing of an assembly with subassemblies; in the graphics area, *face\_or\_edge* **RMB context toolbar > Open Subassembly** |
| **swCommands\_OpenCollaborativeTask** | 3534; valid only in SOLIDWORKS Connected, opens the Collaborative Tasks app in the SOIDWORKS Task Pane; **Lifecycle and Collaboration toolbar > Open Collaborative Task** |
| **swCommands\_OpenFromPC** | 3495; Opens a dialog to select a document on this PC to open in SOLIDWORKS Power-By; **File > Open from This PC...** |
| **swCommands\_OpenInternetAddress** | 130; opens the Open Internet Address dialog; **Web toolbar > Open Internet Address** |
| **swCommands\_Option\_Relations\_Snaps** | 2169; opens the Relations/Snaps page of the System Options dialog for a selected sheet or drawing view in a drawing; in the FeatureManager design tree, *sheet* **RMB menu > Relations/Snaps Options** |
| **swCommands\_Options** | 342; opens the System Options dialog; **Standard toolbar > Options** |
| **swCommands\_OrdinateDimension** | 346; valid for an open sketch; **Dimensions/Relations toolbar > Ordinate Dimension** |
| **swCommands\_Orient\_Annotation\_By\_Selection** | 2216; valid for a selected linear radial dimension; in the graphics area, *lin\_radial\_dim* **RMB menu > Display Options > Orientation > By Selection** |
| **swCommands\_Orient\_Annotation\_View** | 2442; valid for parts and assemblies with a selected active annotation view; in the FeatureManager design tree, *active\_anno\_view* **RMB menu > Orient** |
| **swCommands\_Page\_Setup** | 975; **File menu > Page Setup** |
| **swCommands\_Pan** | 330; **View toolbar > Pan** |
| **swCommands\_Parabola** | 151; **Sketch toolbar > Parabola** |
| **swCommands\_Parallelogram** | 294; opens the Rectangle PropertyManager page; **Sketch tools > Parallelogram** |
| **swCommands\_ParallelSnap** | 526; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; **Quick Snaps toolbar > Parallel Snap** |
| **swCommands\_Parent\_Child\_Rel** | 806; valid for a selected item in the FeatureManager design tree, opens the Parent/Child Relationships dialog; in the FeatureManager design tree, *tree\_item* **RMB menu > Parent/Child** |
| **swCommands\_PartialEllipse** | 86; valid for a selected plane, planar face, or edge on which to create a partial elliptical sketch: **Sketch toolbar > Partial Ellipse** |
| **swCommands\_PartingLines** | 445; valid for parts; **Mold Tools toolbar > Parting Lines** |
| **swCommands\_PartReviewer** | 3058; valid for parts; **Tools toolbar > Part Reviewer** |
| **swCommands\_Paste** | 585; valid for a non-empty clipboard; **Standard toolbar > Paste** |
| **swCommands\_Paste\_Appearance** | 3054; valid for a selection after an appearance has been copied; **Render Tools** or **View toolbar >** **Paste Appearance** |
| **swCommands\_PathLengthDimension** | 3096; valid for an open sketch with selected entities that are end-to-end coincident and form a single chain, opens the Path Length PropertyManager page; **Dimensions/Relations toolbar > Path Length Dimension** |
| **swCommands\_PatternStructConnection** | 3509; Opens the Pattern Connection Element to Corners PropertyManager; **SOLIDWORKS Menu > Insert > Structure System > Pattern Connection Element to Corner** |
| **swCommands\_Pe\_Newsgroup** | 1948; valid on the SOLIDWORKS Personal Edition Help menu |
| **swCommands\_PerimeterCircle** | 545; valid for a selected plane, planar face, or edge, opens the Circle PropertyManager page; **Sketch or Layout Tools toolbar > Perimeter Circle** |
| **swCommands\_PerpendicularSnap** | 527; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; **Quick Snaps toolbar > Perpendicular Snap** |
| **swCommands\_Perspective** | 349; valid for parts and assemblies; **View toolbar > View Settings > Perspective** |
| **swCommands\_Pick\_Identicalcomponents** | 3186; valid for assemblies with a selected component; **Tools menu > Component Selection > Select Identical Components** |
| **swCommands\_PickMode** | 345; places the model in pick mode; **Sketch or Standard toolbar > Select** |
| **swCommands\_Pin\_Orientation\_Dialog** | 2838; valid after **View toolbar > View Orientation > More Options > Orientation dialog; Pin/Unpin the dialog** |
| **swCommands\_Pipe\_Route** | 2270; valid for the SOLIDWORKS Routing add-in, displays the Piping toolbar; **Routing Tools toolbar > Piping** |
| **swCommands\_Pipe\_Rt\_Properties** | 2257; valid for the SOLIDWORKS Routing add-in and an open piping assembly; **Piping toolbar > Route Properties** |
| **swCommands\_Piping\_Custom\_Pipe\_Config** | 1353; valid for a selected reducer route component in a piping drawing or the Input folder of a piping assembly; in the FeatureManager design tree, *reducer\_route\_comp* **RMB menu > Create Custom Pipe Configuration** |
| **swCommands\_Piping\_Make\_Flange\_Driven** | 1356; valid for a selected fitting in a piping drawing or the Input folder of a piping assembly; in the FeatureManager design tree, *comp* **RMB menu > Constrain Fitting to Sketch** |
| **swCommands\_Piping\_Make\_Flange\_Driving** | 1355; valid for a selected fitting in a piping drawing or the Input folder of a piping assembly; in the FeatureManager design tree, *comp* **RMB menu > Constrain Sketch to Fitting** |
| **swCommands\_Piping\_Standard\_Pipe\_Config** | 1354; valid for a selected reducer route component in a custom pipe configuration in a piping drawing or the Input folder of a piping assembly; in the FeatureManager design tree, *reducer\_route\_comp* **RMB menu > Use Standard Pipe\Tube Configuration** |
| **swCommands\_Plane** | 554; valid for a selected reference in a part, opens the Sketch Plane PropertyManager page; **Sketch toolbar > Plane** |
| **swCommands\_PlasticsPremium** | 3493; SOLIDWORKS Plastics Premium |
| **swCommands\_PlasticsPro** | 3492; SOLIDWORKS Plastics Professional |
| **swCommands\_PlasticsStd** | 3491; SOLIDWORKS Plastics Standard |
| **swCommands\_PLM\_Gen\_Derived\_Output\_Number** | 3483; SOLIDWORKS Connected only; Allows you to generate derived output for a selected object; **MySession widget > Action Bar > Tools > Generate Derived Output** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Generate Derived Output** |
| **swCommands\_PLM\_Maturity** | 3476; for SOLIDWORKS Connected only, changes the maturity state of a selected object; **MySession widget > Action Bar > Lifecycle > Maturity** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Maturity** |
| **swCommands\_PLM\_Move\_to** | 3478; SOLIDWORKS Connected only; Allows you to move a selected object to another collaborative space and/or organization and change its owner; **MySession widget > Action Bar > Lifecycle > Move To** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Move To** |
| **swCommands\_PLM\_New\_Revision** | 3477; SOLIDWORKS Connected only; Allows you to create a new revision of a selected object and refresh local information to reflect the new revision; **MySession widget > Action Bar > Lifecycle > New Revision** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > New Revision** |
| **swCommands\_PLM\_Properties** | 3479; SOLIDWORKS Connected only; Displays the 3DEXPERIENCE properties of the selected object; **MySession widget > Action Bar > View > Properties** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > PLM Properties** |
| **swCommands\_PLM\_Relations** | 3480; SOLIDWORKS Connected only; Displays the ecosystem of the related objects by navigating on relationships and paths; **MySession widget > Action Bar > Tools > Relations** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Relations** |
| **swCommands\_PLM\_Reload\_fromServer** | 3474; SOLIDWORKS Connected only; Updates the selected revision in a session with the latest version that exists in 3DEXPERIENCE; **MySession widget > Action Bar > Lifecycle > Reload from Server** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Reload from Server** |
| **swCommands\_PLM\_Replace\_By\_Revision** | 3475; SOLIDWORKS Connected only; Opens the Replace by Revision dialog box to replace the revision that is open in the session; **MySession widget > Action Bar > Lifecycle > Replace by Revision** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Replace by Revision** |
| **swCommands\_PLM\_Replace\_Content** | 3481; SOLIDWORKS Connected only; Opens the File Selection Box in which you can select an object to replace a pre-selected object; **MySession widget > Action Bar > Tools > Replace Content** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Replace Content** |
| **swCommands\_PLM\_Reserve** | 3472; SOLIDWORKS Connected only; Reserves the selected object; **MySession widget > Action Bar > Lifecycle > Reserve** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Reserve** |
| **swCommands\_PLM\_Set\_Ent\_Item\_Number** | 3482; SOLIDWORKS Connected only; Opens the Set Enterprise Item Number dialog box where you can enter the enterprise item number for parts and assemblies; **MySession widget > Action Bar > Tools > Set Enterprise Item Number** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Set Enterprise Item Number** |
| **swCommands\_PLM\_Unreserve** | 3473; SOLIDWORKS Connected only; Removes the reservation of the selected object; **MySession widget > Action Bar > Lifecycle > Unreserve** or **SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Unreserve** |
| **swCommands\_PmCancel** | -1; valid on PropertyManager pages; **Cancel** |
| **swCommands\_PmOK** | -2; valid on PropertyManager pages; **OK** |
| **swCommands\_Point** | 72; valid for a selected plane, planar face, or edge; **Sketch toolbar > Point** |
| **swCommands\_PointSnap** | 521; valid for sketches; **Quick Snaps toolbar > Point Snap** |
| **swCommands\_Polygon** | 305; valid for a selected plane, planar face, or edge, opens the Polygon PropertyManager page; **Sketch tools > Polygon** |
| **swCommands\_Popup\_Hide\_Component** | 812; valid for a selected, visible component; **RMB menu > Hide Component** |
| **swCommands\_Popup\_Hide\_Hidden** | 810; valid for a selected feature with visible edges; **RMB menu > Hide Hidden Edges** |
| **swCommands\_Popup\_Show\_Component** | 811; valid for a selected, hidden component; **RMB menu > Show Component** |
| **swCommands\_Popup\_Show\_Hidden** | 808; valid for a selected feature with hidden edges; **RMB menu > Show Hidden Edges** |
| **swCommands\_Predefined\_Add\_Model** | 2507; valid for a predefined drawing view; *predefined\_drawing\_view* **RMB menu > Insert Model** |
| **swCommands\_PredefinedView** | 428; valid for drawings; **Drawing toolbar > Predefined View** |
| **swCommands\_PrevCmdMgrTab** | 3047; VK\_PRIOR; navigates to the previous CommandManager tab; resource string "Previous CommandManager Tab" |
| **swCommands\_Preview\_Sketch\_Dimension\_Toggle** | 3518; Toggles preview of selected sketch dimension; **Sketch toolbar > Preview Sketch Dimension** |
| **swCommands\_PreviousVersionCheck** | 3523; launches previous release check dialog to check the model for incompatible features; **Tools > Evaluate > Previous Release Check** |
| **swCommands\_PreviousView** | 159; valid for models with changed views; **View toolbar** or **View Orientation dialog > Previous View** |
| **swCommands\_PrimaryAdvStructMember** | 3336; creates a primary structural member feature by sweeping pre-defined profiles along  user-defined paths; **Structures toolbar > Primary Structural Member...** |
| **swCommands\_Print** | 589; valid for an open document, opens the Print dialog; **Standard toolbar > Print** |
| **swCommands\_PrintPreview** | 590; **Standard toolbar > Print Preview** |
| **swCommands\_ProfileProperties** | 3386; creates a predefined pierce point in the weldment profile; **Insert >** **Structure System > Profile Properties** |
| **swCommands\_ProjectCurve** | 74; valid for parts with a selected sketch; **Features toolbar > Curves > Project Curve** |
| **swCommands\_ProjectedView** | 28; valid for a selected drawing view; **Drawing toolbar > Projected View** |
| **swCommands\_Propagate\_Slots** | 3517; Opens Slot Propagation PropertyManager; Propagates slots to a selected instance or all instances of an assembly component containing a tab feature; **RMB menu for selected component with tab feature > Propagate Slots...** |
| **swCommands\_Properties** | 75; opens a Properties dialog for the current selection; **Standard toolbar > Properties** |
| **swCommands\_Properties\_Smart\_Fastener** | 2456; valid for a selected Smart Fastener; *smart\_fastener* **RMB menu > Properties** |
| **swCommands\_Publish\_3DSwym\_3D** | 3503; valid only for **3DEXPERIENCE** platform/SOLIDWORKS Connected; **Tools menu > Lifecycle and Collaboration > Publish to 3DSwym > Share as 3D**; exports the current model as a 3DXML file and publishes it in a 3DSwym community or conversation |
| **swCommands\_Publish\_3DSwym\_Picture** | 3502; valid only for **3DEXPERIENCE** platform/SOLIDWORKS Connected; **Tools** **menu > Lifecycle and Collaboration > Publish to 3DSwym > Share as Picture**; publishes a picture of the current model in a 3DSwym community or conversation |
| **swCommands\_Publish\_Dl\_Content** | 2758; valid for the Motion Study gantt chart and a selected, suppressed simulation element row; in the MotionManager design tree, *rotary\_motor\_bar* **RMB menu > Add to Library** |
| **swCommands\_Publish\_HomeByMe** | 3496; publishes the current document to HomebyMe; **Tools toolbar > Publish to HomeByMe...** |
| **swCommands\_Publish\_To\_Edrawing** | 2931; **Standard toolbar > Publish eDrawings File** |
| **swCommands\_Publish3DPDF** | 3451; **SOLIDWORKS MBD toolbar > Publish to 3D PDF** |
| **swCommands\_PublishSTEP242File** | 3198; **SOLIDWORKS MBD toolbar > Publish STEP 242 File** |
| **swCommands\_PunchTable** | 3036; valid for drawings, opens the Punch Table PropertyManager page; **Table toolbar > Punch Table** |
| **swCommands\_PushPull** | 609; valid for parts, opens the Freeform PropertyManager page; **Features toolbar > Freeform** |
| **swCommands\_QuadrantSnap** | 537; valid for sketches; **Quick Snaps toolbar > Quadrant Snap** |
| **swCommands\_Query\_Advanced** | 1140; valid for assemblies, opens the Advanced Component Selection dialog; **Tools menu > Component Selection > Advanced Select** |
| **swCommands\_Quick\_Create\_Plane** | 1736; valid for a part, opens the Plane PropertyManager page |
| **swCommands\_Rad\_Dim\_Diametric** | 1570; valid for a part with a selected radial dimension; rad*\_dim* **RMB menu > Display Options > Display as Diameter** |
| **swCommands\_Rad\_Dim\_Lindiamtric** | 1571; valid for a part with a selected diameter dimension; *diam\_dim* **RMB menu > Display Options > Display as Linear** |
| **swCommands\_Rad\_Dim\_Radial** | 1568; valid for a part with a selected diameter dimension; *diam\_dim* **RMB menu > Display Options > Display as Radius** |
| **swCommands\_RapidPrototype** | 624; valid for Windows 8.1 or later, opens the Print3D PropertyManager page; **Standard toolbar > Print3D** |
| **swCommands\_RapidSketch** | 2835; **Sketch toolbar > Rapid Sketch** |
| **swCommands\_Re\_Jog** | 3083; valid for a drawing of a circle or arc with a selected angular running dimension; in the graphics area, *angular\_running\_dimensi*on **RMB menu > Display Options > Re-Jog Running Dimension** |
| **swCommands\_Read\_Only\_Pref** | 1905; valid in an open file dialog with preview, **RMB menu > Open as Read-only** |
| **swCommands\_RealviewGraphics** | 499; valid for parts and assemblies; **View toolbar > View Settings > RealView Graphics** |
| **swCommands\_RealViewPlusGraphics** | 500; valid if enabled in the registry (graphics, RealViewPlus\_Enable = 1); **View menu > Display > RealView Plus Graphics** |
| **swCommands\_Reattach\_Dim** | 3521; Re-attaches the selected dangling dimension; **RMB click a dimension > Reattach** |
| **swCommands\_Reattach\_to\_CMarkSet** | 3137; valid for a selected dangling center mark in a drawing; in the graphics area, *dangling\_center\_mark* **RMB menu > Reattach** |
| **swCommands\_Rebuild** | 17; **Standard toolbar > Rebuild** |
| **swCommands\_RebuildAll** | 3200; **Standard toolbar > Rebuild All configuration** |
| **swCommands\_RebuildAndSaveConfig** | 3060; valid for parts and assemblies with multiple configurations; in the ConfigurationManager, *configuration* **RMB menu > Add Rebuild/Save Mark** |
| **swCommands\_RebuildAndSaveConfigActive** | 3; valid for parts and assemblies with multiple configurations; in the ConfigurationManager, *top\_assembly* **RMB menu > Rebuild/Save Mark > Add Mark for This Configuration** |
| **swCommands\_RebuildAndSaveConfigAll** | 3063; valid for parts and assemblies with multiple configurations; in the ConfigurationManager, *top\_assembly* **RMB menu > Rebuild/Save Mark > Add Mark for All Configurations** |
| **swCommands\_RebuildAndSaveConfigOff** | 3061; valid for parts and assemblies with multiple configurations; in the ConfigurationManager, *configuration* **RMB menu > Remove Rebuild/Save Mark** |
| **swCommands\_RebuildAndSaveConfigSpecific** | 3064; valid for parts and assemblies with multiple configurations, opens the Rebuild and Save Settings dialog; in the ConfigurationManager, *top\_assembly* **RMB menu > Rebuild/Save Mark > Add Mark for Specified Configurations** |
| **swCommands\_Recall\_Last\_Render** | 2971; opens the Use perspective Views in Renderings dialog; **Render Tools toolbar > Recall Last Render** |
| **swCommands\_RecordPauseMacro** | 29; **Macro toolbar > Record\Pause Macro** |
| **swCommands\_Rectangle** | 79; valid for a part with a selected plane, planar face, or edge, opens the Rectangle PropertyManager page; **Sketch** or **Layout Tools toolbar > Corner Rectangle** |
| **swCommands\_RectangleAtAngle** | 2793; valid for a part with a selected plane, planar face, or edge, opens the Rectangle PropertyManager page; **Sketch** or **Layout Tools toolbar > 3 Ponit Corner Rectangle** |
| **swCommands\_Redo** | 587; valid for a model for which an Undo action occurred; **Standard toolbar > Redo** |
| **swCommands\_Redraw** | 355; **View toolbar > Redraw** |
| **swCommands\_Ref\_Help** | 771; **Edit Referenced File Locations dialog > Help** |
| **swCommands\_Reference\_arrow** | 3138; valid for a selected component in an assembly; *comp* **RMB menu context toolbar > Dynamic Reference Visualization (Parent)** |
| **swCommands\_ReferenceGeometry** | 484; alternative to swCommands\_Toolbar\_Refgeom; **View menu > Toolbars > Reference Geometry** |
| **swCommands\_RefPlane\_Flip\_Normal** | 3113; valid for a selected reference plane in a part; in the graphics area, *ref\_plane* **RMB context toolbar > Flip Normal** |
| **swCommands\_Reimport\_From\_To\_Lst** | 2861; valid for a SOLIDWORKS Routing add-in and an assembly to which from-to list was imported; **Electrical toolbar > Re-Import From/To** |
| **swCommands\_RelativeView** | 27; valid for a drawing with a selected planar face, opens the Relative View PropertyManager page; **Drawing toolbar > Relative View** |
| **swCommands\_Reload** | 1618; P**alette toolbar >** **Reload** |
| **swCommands\_Remove\_Body\_Appearance** | 2935; valid in a body appearance callout; *body\_appearance\_callout* **RMB menu context toolbar > This instance** |
| **swCommands\_Remove\_Component\_Appearance** | 2936; valid in a component appearance callout; *comp\_appearance\_callout* **RMB menu context toolbar > This instance** |
| **swCommands\_Remove\_Feature\_Appearance** | 2934; valid in a feature appearance callout; *feature\_appearance\_callout* **RMB menu context toolbar > This instance** |
| **swCommands\_Remove\_Feature\_Dims** | 1553; valid for a selected, dimensioned feature; in the FeatureManager design tree,*feature* **RMB menu > HideAll Dimensions** |
| **swCommands\_Remove\_From\_ChainDim** | 3412; valid for a selected dimension in a chain dimension set, makes the selected dimension independent from the chain dimension set; **RMB menu > Convert To Chain** |
| **swCommands\_Remove\_From\_Library** | 1525; valid for a selected library feature; in the FeatureManager design tree, *lib\_feat* **RMB menu > Remove From Library** |
| **swCommands\_Remove\_Mark\_LDR\_AndPurgeDataForAllConfig** | 3209; valid for an assembly opened in Resolved or Lightweight mode, allows the user to unmark the configurations to display for the assembly opened in Large Design Review mode; in the ConfigurationManager, *top\_level\_assembly* **RMB menu > Large Design Review Mark > Remove Mark and Purge Data for All Configurations** |
| **swCommands\_Remove\_Part\_Appearance** | 2937; valid in a part appearance callout; *part\_appearance\_callout* **RMB menu context toolbar > This instance** |
| **swCommands\_Remove\_Smc\_Reference** | 2677; valid in Missing Reference list boxes of PropertyManager pages; *list\_box\_item* **RMB menu > Delete** |
| **swCommands\_Remove\_Snap** | 1554; valid for a drawing with a selected dimension extension line endpoint configured with a snap option; *dim\_ext\_line\_endpt\_with\_snap* **RMB menu > Display Options > Default Extension Snap** |
| **swCommands\_RemoveAllDisplayStates** | 3037; valid for a part that is not in edit mode; in the ConfigurationManager, *white\_space* **RMB menu > Remove all display states** |
| **swCommands\_RemovedSection** | 3352; adds a removed section view; **Drawing toolbar > Removed Section** |
| **swCommands\_RemoveMarkAndPurgeDataForAllConfig** | 3091; valid for parts and assemblies with multiple configurations; in the ConfigurationManager, *top\_assem*bly **RMB menu > Rebuild/Save Mark > Remove Mark and Purge Data for All Configurations** |
| **swCommands\_RemoveMateMisalignment** | 3327; valid for pre-selected concentric misaligned mate, removes its mate misalignment property; in the FeatureManager design tree, concentric mate **RMB menu > Remove misalignment** |
| **swCommands\_Rename\_Annotation\_View** | 3136; valid for a selected annotation view in the Select Annotation View dialog; *anno\_view* **RMB menu > Rename** |
| **swCommands\_Render\_Options** | 2968; **Render Tools toolbar > Options** |
| **swCommands\_Render\_Region** | 3115; **Render Tools toolbar > Render Region** |
| **swCommands\_RenderToolbar** | 2962; alternative to swCommands\_Toolbar\_Render; **View menu > Toolbars > Render Tools** |
| **swCommands\_Renumber\_Hole\_Table** | 2964; valid for drawings with hole tables; in the FeatureManager design tree, *hole\_table* **RMB menu > Renumber all Tags** |
| **swCommands\_Renumber\_Series\_Table** | 2965; valid for a selected row in the TAG column of a drawing hole table; in the graphics area, *hole\_table\_row\_tag\_column* **RMB menu > Renumber Series** |
| **swCommands\_Repair\_Route** | 2289; valid for the SOLIDWORKS Routing add-in and an open routing assembly; **Routing Tools toolbar > Repair Route** |
| **swCommands\_RepairSketch** | 380; valid only for sketches in edit mode; **Sketch toolbar > Repair Sketch** |
| **swCommands\_Repeat\_Command** | 2114; **Edit menu > Repeat Last Command** |
| **swCommands\_Repeat\_Mate** | 2819; valid for selected components in an assembly, opens the Copy with Mates PropertyManager page; **Assembly toolbar > Copy with Mates** |
| **swCommands\_ReplaceComponents** | 575; valid for assemblies, opens the Replace PropertyManager page; **Assembly toolbar > Replace Components** |
| **swCommands\_ReplaceEntity** | 3104; valid for a selected sketch entity in an open sketch, opens the Replace Entity PropertyManager page; **Sketch toolbar > Replace Entity** |
| **swCommands\_ReplaceFace** | 371; valid for a solid or surface body, opens the Replace Face1 PropertyManager page; **Surface toolbar > Replace Face** |
| **swCommands\_ReplaceFormTool** | 3024; valid for parts with a Forming Tool, opens the Open dialog; in the FeatureManager design tree, *forming\_tool* **RMB menu > Replace Form Tool** |
| **swCommands\_ReplaceMateEntities** | 574; valid for a selected Mate Group entity in assemblies; in the FeatureManager design tree, **Assembly toolbar > Replace Mate Entities** |
| **swCommands\_Reset** | 635; *dialog* **> Reset** |
| **swCommands\_Reset\_Dim\_Extension\_Centerline** | 3107; valid for a drawing with a centered dimension extension line; in the graphics area, *dim\_ext\_line* **RMB menu > Reset Extension Line Style** |
| **swCommands\_Reset\_Line\_Font** | 1575; valid for a selected drawing edge whose line format was changed from the default; in the graphics area, *sel\_edge* **RMB menu > Reset line font** |
| **swCommands\_Reset\_Std\_View** | 700; valid after **View toolbar > View Orientation > More Options** is selected; **Orientation dialog > Reset Standard Views** |
| **swCommands\_Resolve\_All** | 1234; valid for selected assembly with lightweight components; in the FeatureManager design tree, *top\_level\_assy* **RMB menu > Set Lightweight to Resolved** |
| **swCommands\_Resolve\_Conflict** | 2192; valid for an open, over-defined sketch, opens the SketchXpert PropertyManager page; **Tools menu > Sketch Tools > SketchXPert** |
| **swCommands\_Resolve\_Drawing** | 3447; valid only for drawings in Detailing mode; **FeatureManager design tree root node RMB menu > Resolve drawing** or first button in every CommandManager toolbar |
| **swCommands\_Resolve\_Mate\_Component\_1** | 2532; valid for an assembly with two lightweight mate components, one of which is suppressed; in the FeatureManager design tree, *unsuppressed\_lightweight\_mate\_component* **> Mates in** *assy\_name* **>** *constraint\_of\_suppressed\_lightweight\_mate\_component\_1* **RMB menu >** *supp\_ltwt\_mate\_comp\_1* **> Resolve component** |
| **swCommands\_Resolve\_Mate\_Component\_2** | 2537; valid for an assembly with a mate containing three lightweight mate components, two of which are suppressed; in the FeatureManager design tree, *unsuppressed\_lightweight\_mate\_component* **> Mates in** *assy\_name* **>** *constraint\_of\_suppressed\_lightweight\_mate\_component\_2* **RMB menu >** *supp\_ltwt\_mate\_comp\_2* **> Resolve component** |
| **swCommands\_Resolve\_Out\_Of\_Date\_Lwcomps** | 1407; valid for a selected assembly with out-of-date lightweight components; *top\_assy* **RMB menu > Set out-of-date Lightweight to Resolved** |
| **swCommands\_Resolve\_Top** | 3034; valid for a selected assembly opened in Large Design Review mode; in the FeatureManager design tree, *top\_assy* **RMB menu > Set All to Resolved** |
| **swCommands\_Resolve\_Top\_LightWeight** | 3035; valid for a selected assembly opened in Large Design Review mode; in the FeatureManager design tree, *top\_assy* **RMB menu > Set All to Lightweight** |
| **swCommands\_Restore\_Align** | 1513; valid only for a selected drawing view that has been aligned; in the FeatureManager design tree, *sel\_align\_view* **RMB menu > Alignment > Default Alignment** |
| **swCommands\_Restore\_Rotation** | 637; valid for a selected drawing view that has been rotated; in the FeatureManager design tree, *sel\_rot\_view* **RMB menu > Alignment > Default Rotation** |
| **swCommands\_Restore\_Settings** | 3114; **Tools menu > Save/Restore Settings** |
| **swCommands\_Resume\_Stacking\_Balloons** | 676; valid for a selected balloon in a drawing view, opens the Stacked Balloon PropertyManager page; *sel\_balloon* **RMB menu > Add to Stack** |
| **swCommands\_Reverse\_Endpoint\_Tangency** | 3304; **Sketch toolbar > Reverse Endpoint Tangent** |
| **swCommands\_Review\_Pending\_Updates** | 2989; valid for a selected frozen feature that has updates pending due to the lock, opens a What's Wrong dialog with the pending updates; in the FeatureManager design tree, *frozen\_feature* **RMB menu > Review Pending Updates**; resource string "Show all pending updates due to Freeze. Review Pending Updates" |
| **swCommands\_RevisionCloud** | 3052; valid for drawings, opens the Revision Cloud PropertyManager page; **Annotation toolbar > Revision Cloud** |
| **swCommands\_RevisionSymbol** | 457; valid for a drawing with a revision table with one or more revision rows; **Annotation toolbar > Revision Symbol** |
| **swCommands\_RevisionTable** | 456; valid for drawings, opens the Revision Table PropertyManager page; **Table toolbar > Revision Table** |
| **swCommands\_RevolvedBossBase** | 24; valid for parts with a selected sketch; **Features toolbar > Revolved Boss/Base** |
| **swCommands\_RevolvedCut** | 48; valid for parts with a selected sketch; **Features toolbar > Revolved Cut** |
| **swCommands\_RevolvedSurface** | 104; valid for a selected profile and the centerline about which to revolve the surface, opens the Surface-Revolve PropertyManager page; **Surfaces toolbar > Revolve Surface** |
| **swCommands\_Rib** | 125; valid for parts with a selected sketch, opens the Rib1 PropertyManager page; **Features toolbar > Rib** |
| **swCommands\_Right** | 165; **View toolbar > View Orientation > Right** |
| **swCommands\_Rip** | 297; valid for sheet metal parts; **Sheet Metal toolbar > Rip** |
| **swCommands\_Rip\_Both\_Directions** | 1707; valid when inserting a sheet metal rip; in the graphics area, *rip\_manipulator* **RMB menu > Both Directions** |
| **swCommands\_Rip\_Single\_Direction** | 1708; valid when inserting a sheet metal rip; in the graphics area, *rip\_manipulator* **RMB menu > Single Direction** |
| **swCommands\_Rmb\_Ann\_Use\_Jog\_Leader** | 1808; valid for a new drawing annotation; in the graphics area, *new\_anno* **RMB menu > Use Multi-jog Leader** |
| **swCommands\_Rmb\_Appear\_Callout\_Delete\_Body\_Color** | 2696; valid for a selected body row in an appearance callout; **RMB menu > Remove Color** |
| **swCommands\_Rmb\_Appear\_Callout\_Delete\_Body\_Texture** | 2697; valid for a selected body row in an appearance callout; **RMB menu > Remove Texture** |
| **swCommands\_Rmb\_Appear\_Callout\_Delete\_Comp\_Color** | 2698; valid for a selected component row in an appearance callout; **RMB menu > Remove Color** |
| **swCommands\_Rmb\_Appear\_Callout\_Delete\_Comp\_Texture** | 2699; valid for a selected component row in an appearance callout; **RMB menu > Remove Texture** |
| **swCommands\_Rmb\_Appear\_Callout\_Delete\_Face\_Color** | 2685; valid for a selected face row in an appearance callout; **RMB menu > Remove Color** |
| **swCommands\_Rmb\_Appear\_Callout\_Delete\_Face\_Texture** | 2686; valid for a selected face row in an appearance callout; **RMB menu > Remove Texture** |
| **swCommands\_Rmb\_Appear\_Callout\_Delete\_Feat\_Color** | 2694; valid for a selected feature row in an appearance callout; **RMB menu > Remove Color** |
| **swCommands\_Rmb\_Appear\_Callout\_Delete\_Feat\_Texture** | 2695; valid for a selected feature row in an appearance callout; **RMB menu > Remove Texture** |
| **swCommands\_Rmb\_Appear\_Callout\_Delete\_Part\_Color** | 2700; valid for a selected part row in an appearance callout; **RMB menu > Remove Color** |
| **swCommands\_Rmb\_Appear\_Callout\_Delete\_Part\_Texture** | 2701; valid for a selected part row in an appearance callout; **RMB menu > Remove Texture** |
| **swCommands\_Rmb\_Appear\_Callout\_Edit\_Body\_Color** | 2688; valid for a selected body row in an appearance callout; **RMB menu > Edit Color** |
| **swCommands\_Rmb\_Appear\_Callout\_Edit\_Body\_Texture** | 2691; valid for a selected body row in an appearance callout; **RMB menu > Edit Texture** |
| **swCommands\_Rmb\_Appear\_Callout\_Edit\_Color** | 2649; valid for a selected face row in an appearance callout; **RMB menu > Edit Color** |
| **swCommands\_Rmb\_Appear\_Callout\_Edit\_Comp\_Color** | 2702; valid for a selected component row in an appearance callout; **RMB menu > Edit Color** |
| **swCommands\_Rmb\_Appear\_Callout\_Edit\_Comp\_Texture** | 2703; valid for a selected component row in an appearance callout; **RMB menu > Edit Texture** |
| **swCommands\_Rmb\_Appear\_Callout\_Edit\_Feat\_Color** | 2687; valid for a selected feature row in an appearance callout; **RMB menu > Edit Color** |
| **swCommands\_Rmb\_Appear\_Callout\_Edit\_Feat\_Texture** | 2690; valid for a selected feature row in an appearance callout; **RMB menu > Edit Texture** |
| **swCommands\_Rmb\_Appear\_Callout\_Edit\_Part\_Color** | 2689; valid for a selected part row in an appearance callout; **RMB menu > Edit Color** |
| **swCommands\_Rmb\_Appear\_Callout\_Edit\_Part\_Texture** | 2692; valid for a selected part row in an appearance callout; **RMB menu > Edit Texture** |
| **swCommands\_Rmb\_Appear\_Callout\_Edit\_Texture** | 2650; valid for a selected face row in an appearance callout; **RMB menu > Edit Texture** |
| **swCommands\_Rmb\_Appearance\_Co** | 2646; valid for a selected face, displays an appearance callout in the graphics area |
| **swCommands\_Rmb\_BiDir** | 3383; valid when the Projected Curve PropertyManager is active, **graphics area RMB menu > Bi-Directional Projection** |
| **swCommands\_RMB\_Blind\_Direction\_2** | 3072; valid when the Surface-Revolve PropertyManager page is open, and Direction 1 is not set to Mid Plane; in the graphics area, *revolve\_sketch* **RMB menu > Direction 2 > Blind** |
| **swCommands\_Rmb\_Bodyappearance\_Co** | 2679; valid for a selected solid body, displays an appearance callout in the graphics area |
| **swCommands\_Rmb\_Collect\_All\_Bends** | 730; valid for sheet metal parts when the Fold PropertyManager page is open; in the graphics area, **RMB menu > Collect All Bends** |
| **swCommands\_Rmb\_Compappearance\_Co** | 2680; valid for a selected component, displays an appearance callout in the graphics area |
| **swCommands\_Rmb\_Cpat\_Equal\_Space** | 1660; valid when a Circular Pattern PropertyManager page is open for a non-dimension circular pattern; in the graphics area, **RMB menu > Equal Spacing**; valid only if swCommands\_Rmb\_Cpat\_Symmetric is called |
| **swCommands\_Rmb\_Cpat\_Equal\_Spacing1** | 3213; valid when a Circular Pattern PropertyManager page is open for a non-dimension circular pattern; in the graphics area, **RMB menu > Equal Spacing Direction 1**; not valid if swCommands\_Rmb\_Cpat\_Symmetric is called; see swCommands\_Rmb\_Cpat\_Equal\_Space |
| **swCommands\_Rmb\_Cpat\_Equal\_Spacing2** | 3214; valid when a Circular Pattern PropertyManager page is open for a non-dimension circular pattern; in the graphics area, **RMB menu > Equal Spacing Direction 2**; not valid if swCommands\_Rmb\_Cpat\_Symmetric is called; see swCommands\_Rmb\_Cpat\_Equal\_Space |
| **swCommands\_Rmb\_Cpat\_Flip\_Direction** | 1667; valid when a Circular Pattern PropertyManager page is open; in the graphics area, **RMB menu > Reverse Direction** |
| **swCommands\_Rmb\_Cpat\_Geometry\_Pattern** | 1661; valid when a Circular Pattern PropertyManager page is open for a non-dimension, non-body circular pattern in an assembly that is not in edit mode; in the graphics area, **RMB menu > Geometry Pattern** |
| **swCommands\_Rmb\_Cpat\_Symmetric** | 3192; valid when a Circular Pattern PropertyManager page is open; in the graphics area, **RMB menu > Symmetric** |
| **swCommands\_Rmb\_Create\_Hole\_Series** | 2660; valid for a selected assembly Wizard Hole; in the FeatureManager design tree, *wizard\_hole\_feature* **RMB menu > Create Hole Series** |
| **swCommands\_Rmb\_Delete\_Manipulator** | 2500; valid for a selected manipulator for some dialogs (mold shut-off surface and fillet); **RMB menu > Delete** |
| **swCommands\_RMB\_Direction\_2\_OnOff** | 3079; valid when the Surface-Revolve PropertyManager page is open, and Direction 1 is not set to Mid Plane; in the graphics area, *revolve\_sketch* **RMB menu > Direction 2 > Direction 2 Off** |
| **swCommands\_Rmb\_Display\_Camera\_FOV\_Box** | 2840; valid for a model with a selected camera in DisplayManager; in the display area, **RMB menu > Display Field of View Box** |
| **swCommands\_Rmb\_Edit\_Camera** | 1059; valid for a model with a selected camera in DisplayManager; **Camera >** *Camera1* **RMB menu > Edit Camera** |
| **swCommands\_Rmb\_Edit\_Section** | 753; valid for a section view; in the graphics area of a section view, **RMB menu > Section View Properties** |
| **swCommands\_Rmb\_Edit\_SimResults** | 3202; opens the View Simulation Results PropertyManager page; valid only if the SOLIDWORKS Simulation add-in is loaded, Simulation study results are available for the current model, **View toolbar > View Simulation Results** was previously clicked, and the View Simulation Results PropertyManager page was configured to display simulation results with the model; in the graphics area, **RMB menu > Simulation Results Properties** |
| **swCommands\_Rmb\_Enable\_Appear\_Callouts** | 2704; **Appearance Callout dialog > Enable Appearance Callouts** |
| **swCommands\_Rmb\_Extend\_Distance** | 1664; valid when the Surface-Extend1 PropertyManager page is open; in the graphics area, *surface\_extend\_sketch* **RMB menu > Distance** |
| **swCommands\_Rmb\_Extend\_Upto\_Point** | 1665; valid when the Surface-Extend1 PropertyManager page is open; in the graphics area, *surface\_extend\_sketch* **RMB menu > Up to Point** |
| **swCommands\_Rmb\_Extend\_Upto\_Surface** | 1666; valid when the Surface-Extend1 PropertyManager page is open; in the graphics area, *surface\_extend\_sketch* **RMB menu > Up to Surface** |
| **swCommands\_Rmb\_Face\_Zebra\_Stripes** | 1807; valid for a selected face, opens the Zebra Stripes PropertyManager page; *sel\_face* **RMB menu > Zebra Stripes** |
| **swCommands\_Rmb\_Featappearance\_Co** | 2678; valid for a selected feature, displays an appearance callout in the graphics area |
| **swCommands\_Rmb\_Find\_Intersection** | 3110; use to define virtual sharps; valid for an open sketch while in the dimension tool; in the graphics area, *sketch\_entity* **RMB menu > Find Intersection** |
| **swCommands\_Rmb\_Iso\_Ad\_Mesh** | 731; valid when the Face Curves PropertyManager page is open, and Position is selected; in the graphics area, **RMB menu > Mesh** |
| **swCommands\_Rmb\_Iso\_Constrain\_Model** | 733; valid when the Face Curves PropertyManager page is open; in the graphics area, **RMB menu > Constrain to Model** |
| **swCommands\_Rmb\_Iso\_Ignore\_Holes** | 734; valid when the Face Curves PropertyManager page is open; in the graphics area, **RMB menu > Ignore Holes** |
| **swCommands\_Rmb\_Iso\_Position** | 732; valid when the Face Curves PropertyManager page is open, and Mesh is selected; in the graphics area, **RMB menu > Position** |
| **swCommands\_Rmb\_Leader\_Done** | 2475; valid for drawings while adding an annotation leader; *anno\_leader* **RMB menu > End Leader (double click)** |
| **swCommands\_Rmb\_Lock\_Camera** | 1062; valid when a model is in Camera View mode; in the graphics area, **RMB menu > Lock Camera** |
| **swCommands\_Rmb\_Loft\_Close** | 726; valid when the Surface-Loft PropertyManager page is open; in the graphics area, *loft\_sketch* **RMB menu > Close Loft** |
| **swCommands\_Rmb\_Loft\_Mesh\_Allfaces1** | 2630; valid when the Boundary-Surface PropertyManager page is open, and two directions are selected; in the graphics area, **RMB menu > Mesh Preview > Mesh All Faces** |
| **swCommands\_Rmb\_Loft\_Mesh\_Clear\_Allfaces1** | 2632; valid when the Boundary-Surface PropertyManager page is open, two directions are selected, and all faces are meshed; in the graphics area, **RMB menu > Mesh Preview > Clear All Meshed Faces** |
| **swCommands\_Rmb\_Loft\_Mesh\_Clear\_Oneface1** | 2633; valid when the Boundary-Surface PropertyManager page is open, and a face is meshed; in the graphics area, **RMB menu > Mesh Preview > Clear Meshed Faces** |
| **swCommands\_Rmb\_Loft\_Mesh\_Oneface1** | 2631; valid when the Boundary-Surface PropertyManager page is open; in the graphics area, **RMB menu > Mesh Preview > Mesh Face** |
| **swCommands\_Rmb\_Loft\_Show\_All** | 2525; valid when the Loft PropertyManager page is open, and connectors have been hidden; in the graphics area, **RMB menu > Show All Connectors** |
| **swCommands\_Rmb\_Loft\_Synch\_Hide** | 2522; valid when the Loft PropertyManager page is open, and a connector is selected; in the graphics area, *connector* **RMB menu > Hide Connector** |
| **swCommands\_Rmb\_Loft\_Synch\_Hide\_All** | 2524; valid when the Loft PropertyManager page is open; in the graphics area, **RMB menu > Hide All Connectors** |
| **swCommands\_Rmb\_Loft\_Synch\_Undo** | 2523; valid when the Surface-Loft PropertyManager page is open; in the graphics area, **RMB menu > Reset Connectors** |
| **swCommands\_Rmb\_Loft\_Synch\_Undo\_Last\_Oper** | 2611; valid when the Loft PropertyManager page is open, and a connector has been deleted; in the graphics area, **RMB menu > Undo connector edit** |
| **swCommands\_Rmb\_Loft\_Tangency** | 724; valid when the Surface-Loft PropertyManager page is open; in the graphics area, *loft\_sketch* **RMB menu > Merge tangent faces** |
| **swCommands\_Rmb\_Mvsrf\_Copy** | 746; valid when the Move Face PropertyManager page is open; in the graphics area, **RMB menu > Copy** |
| **swCommands\_RMB\_OffsetFromSurface\_Direction\_2** | 3075; valid when the Surface-Revolve PropertyManager page is open, and Direction 1 is not set to Mid Plane; in the graphics area, *revolve\_sketch* **RMB menu > Direction 2 > Offset From Surface** |
| **swCommands\_Rmb\_Onto\_Face** | 2473; valid when the Projected Curve PropertyManager page is open, and Projection type is Sketch on sketch; in the graphics area, **RMB menu > Sketch onto Face(s)** |
| **swCommands\_Rmb\_Onto\_Sketch** | 2472; valid when the Projected Curve PropertyManager page is open, and Projection type is Sketch on faces; in the graphics area, **RMB menu > Sketch onto Sketch** |
| **swCommands\_Rmb\_Reverse** | 2474; valid when the Projected Curve PropertyManager page is open; in the graphics area, **RMB menu > Reverse Projection** |
| **swCommands\_RMB\_Reverse\_Direction** | 3080; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, *revolve\_sketch* **RMB menu > Direction 1 > Reverse Direction** |
| **swCommands\_Rmb\_Rib\_Both\_Sides** | 1791; valid when the Rib1 PropertyManager page is open; in the graphics area, **RMB menu > Both Sides** |
| **swCommands\_Rmb\_Rib\_First\_Side** | 1789; valid when the Rib1 PropertyManager page is open; in the graphics area, **RMB menu > First Side** |
| **swCommands\_Rmb\_Rib\_Normal\_To\_Sketch** | 1792; valid when the Rib1 PropertyManager page is open, and Extrusion direction is Parallel to Sketch; in the graphics area, **RMB menu > Normal to Sketch** |
| **swCommands\_Rmb\_Rib\_Parallel\_To\_Sketch** | 1793; valid when the Rib1 PropertyManager page is open, and Extrusion direction is Normal to Sketch; in the graphics area, **RMB menu > Parallel to Sketch** |
| **swCommands\_Rmb\_Rib\_Second\_Side** | 1790; valid when the Rib1 PropertyManager page is open, and Extrusion direction is Parallel to Sketch; in the graphics area, **RMB menu > Second Side** |
| **swCommands\_Rmb\_Skcham\_Angle** | 736; valid when the Sketch Chamfer PropertyManager page is open, and Distance-distance is selected; in the graphics area, **RMB menu > Angle-Distance** |
| **swCommands\_Rmb\_Skcham\_Dist** | 735; valid when the Sketch Chamfer PropertyManager page is open, and Angle-distance is selected; in the graphics area, **RMB menu > Distance-Distance** |
| **swCommands\_Rmb\_Skcham\_Equal** | 737; valid when the Sketch Chamfer PropertyManager page is open, and Distance-distance is selected; in the graphics area, **RMB menu > Equal Distance** |
| **swCommands\_Rmb\_Sm\_Bend\_Revdir** | 739; valid when the Sketched Bend PropertyManager page is open; in the graphics area, **RMB menu > Reverse Direction** |
| **swCommands\_Rmb\_Sm\_Reverse\_Dir** | 738; valid when the Revolve PropertyManager page is open, and Thin Feature is selected; in the graphics area, **RMB menu > Reverse Direction (second version)** |
| **swCommands\_Rmb\_Spat\_Centroid** | 1662; valid when a Sketch Driven Pattern PropertyManager page is open, and Reference point is Selected point; in the graphics area, **RMB menu > Bounding box center** |
| **swCommands\_Rmb\_Spat\_Geometry\_Pattern** | 1663; valid when a Sketch Driven Pattern PropertyManager page is open; in the graphics area, **RMB menu > Geometry Pattern** |
| **swCommands\_Rmb\_Spat\_Selpoint** | 1773; valid when a Sketch Driven Pattern PropertyManager page is open, and Reference point is Centroid; in the graphics area, **RMB menu > Selected point** |
| **swCommands\_Rmb\_Sweep\_Align** | 729; valid when the Cut-Sweep PropertyManager page is open; in the graphics area, **RMB menu > Align with end faces** |
| **swCommands\_Rmb\_Sweep\_Tangency** | 727; valid when the Surface-Sweep PropertyManager page is open; in the graphics area, *sweep\_sketch* **RMB menu > Merge tangent faces** |
| **swCommands\_RMB\_Throughall\_Direction\_2** | 3076; valid when the Cut-Extrude PropertyManager page is open; in the graphics area, **RMB menu > Direction 2 > Through All** |
| **swCommands\_RMB\_ThroughNext\_Direction\_2** | 3077; valid when the Cut-Extrude PropertyManager page is open; in the graphics area, **RMB menu > Direction 2 > Up To Next** |
| **swCommands\_RMB\_UptoBody\_Direction\_2** | 3078; valid when the Surface-Extrude PropertyManager page is open; in the graphics area, *extrude\_sketch* **RMB menu > Direction 2 > Up To Body** |
| **swCommands\_RMB\_UptoSurface\_Direction\_2** | 3074; valid when the Surface-Revolve PropertyManager page is open, and Direction 1 is not set to Mid Plane; in the graphics area, *revolve\_sketch* **RMB menu > Direction 2 > Up To Surface** |
| **swCommands\_RMB\_UptoVertex\_Direction\_2** | 3073; valid when the Surface-Revolve PropertyManager page is open, and Direction 1 is not set to Mid Plane; in the graphics area, *revolve\_sketch* **RMB menu > Direction 2 > Up To Vertex** |
| **swCommands\_Rmb\_Zebra\_Properties** | 1761; valid for a model with zebra stripes, opens the Zebra Stripes PropertyManager page; in the graphics area, **RMB menu >** **Zebra Stripe Properties** |
| **swCommands\_RMBFreeshapeCancel** | 3320; cancels FreeShape; **FreeShape RMB menu > Cancel** |
| **swCommands\_RMBFreeshapeOK** | 3319; **FreeShape RMB menu > OK** |
| **swCommands\_Roll** | 605; **View toolbar > Roll** |
| **swCommands\_RotaryMotor** | 423; **MotionManager toolbar > Motor** |
| **swCommands\_Rotate\_180\_Degrees** | 2278; valid when the move triad is visible; in the graphics area, *triad\_ring* **RMB menu > rotate 180⁰** |
| **swCommands\_Rotate\_45\_Degrees** | 2880; valid for a selected ZX triad ring of a live section plane; in the graphics area, *ZX\_triad\_ring* **RMB menu > rotate 45⁰** |
| **swCommands\_Rotate\_90\_Degrees** | 2277; valid when the move triad is visible; in the graphics area, *triad\_ring* **RMB menu > rotate 90⁰** |
| **swCommands\_Rotate\_Routing\_Clip** | 1637; valid for the SOLIDWORKS Routing add-in with a selected routing clip in an open routing assembly; **Routing Tools toolbar > Rotate Clip** |
| **swCommands\_Rotate\_Show\_Delta\_Xyz** | 1136; valid after *component* **RMB menu > Move with Triad** command in an assembly; in the graphics area, *triad\_center\_ball* **RMB menu > Show Rotate Delta XYZ Box** |
| **swCommands\_Rotate\_Xaxis\_By90** | 3132; valid when the Insert Component PropertyManager page is open, and a part or assembly to insert is selected; in the graphics area, **RMB menu > Rotate X 90 Deg** |
| **swCommands\_Rotate\_Yaxis\_By90** | 3133; valid when the Insert Component PropertyManager page is open, and a part or assembly to insert is selected; in the graphics area, **RMB menu > Rotate Y 90 Deg** |
| **swCommands\_Rotate\_Zaxis\_By90** | 3134; valid when the Insert Component PropertyManager page is open, and a part or assembly to insert is selected; in the graphics area, **RMB menu > Rotate Z 90 Deg** |
| **swCommands\_RotateComponent** | 21; valid for assemblies; **Tools menu > Component > Rotate** or **Assembly toolbar > Rotate Component** |
| **swCommands\_RotateEntities** | 503; valid for a sketch with a selected entity or annotation; **Sketch toolbar > Rotate Entities** |
| **swCommands\_RotateView** | 329; **View toolbar > Rotate View** |
| **swCommands\_Route\_Add\_To\_Fab** | 1328; valid for the SOLIDWORKS Routing add-in, an open routing assembly, and a selected connection point or component; in the graphics area, *cpoint\_or\_comp* **RMB menu > Add to Route** |
| **swCommands\_Route\_Get\_Property** | 721; valid for the SOLIDWORKS Routing add-in with a selected routing segment in an open routing assembly; in the graphics area, *route\_segment* **RMB menu > Route Segment Properties** |
| **swCommands\_Route\_Io\_Output** | 2397; valid for the SOLIDWORKS Routing add-in and an open pipe or tube routing assembly; in the graphics area, *route\_pipe\_or\_tube* **RMB menu > Export Pipe/Tube Data** |
| **swCommands\_Route\_Properties** | 693; valid for the SOLIDWORKS Routing add-in and an open piping route, opens the Route Properties PropertyManager page; **Piping toolbar > Route Properties** |
| **swCommands\_Route\_Realign\_Fitting** | 1326; valid for the SOLIDWORKS Routing add-in with an open routing assembly and a selected piping fitting; in the graphics area, *sel\_piping\_fitting* **RMB menu > Change Fitting Alignment** |
| **swCommands\_Route\_Remove\_Pipe** | 723; valid for the SOLIDWORKS Routing add-in with an open routing assembly and a selected pipe; in the graphics area, *sel\_pipe* **RMB menu > Remove Pipe** |
| **swCommands\_Route\_Rotate\_Clip** | 2266; valid for SOLIDWORKS Routing add-in and an open routing assembly; **Routing Tools toolbar > Rotate Clip** |
| **swCommands\_Route\_Start\_Con\_Point** | 1238; valid for the SOLIDWORKS Routing add-in with a selected component in a route that is not in edit mode; in the graphics area, *comp* **RMB menu > Start Route** |
| **swCommands\_Route\_Through** | 2267; valid for the SOLIDWORKS Routing add-in and an open route; **Routing Tools toolbar > Route Through Clip** |
| **swCommands\_Route\_Unhook\_From** | 2268; valid for SOLIDWORKS Routing add-in and an open route; **Routing Tools toolbar > Unhook from Clip** |
| **swCommands\_RouteLine** | 396; valid for the SOLDWORKS Routing add-in and an open route; **Explode Sketch toolbar > Route Line** |
| **swCommands\_Router\_Change\_Mode** | 2558; valid for the SOIDWORKS Routing add-in, when the Auto Route PropertyManager page is open, and Auto Route Orthogonal route is selected; in the graphics area, **RMB menu > Edit Mode** |
| **swCommands\_Routing\_Reuse\_Route** | 3190; valid for the SOLIDWORKS Routing add-in and an open electrical routing assembly; **Electrical toolbar > Reuse Route** |
| **swCommands\_Routing\_Tools** | 2448; valid for the SOLIDWORKS Routing add-in; **Route toolbar > Routing Tools** |
| **swCommands\_RunMacro** | 30; **Macro toolbar > Run Macro** |
| **swCommands\_SageExpress** | 2952; valid for parts, opens the Enable SustainabilityXpress dialog; **Tools toolbar > SustainabilityXpress** |
| **swCommands\_Save** | 2; for modified parts, opens the Save Modified Documents dialog; **Standard toolbar > Save** or **Older version file** |
| **swCommands\_Save\_Comp** | 2118; valid for shared assemblies in a multi-user environment (select **Tools > Options > System Options > Collaboration > Add shortcut menu items for multi-user environment**; in the FeatureManager design tree, *comp* **RMB menu > Save** |
| **swCommands\_Save\_Config\_Preview** | 1853; valid for a document that is already saved, saves a configuration preview |
| **swCommands\_Save\_Journal\_As\_Word** | 2060; valid for a selected journal, saves it in Word format |
| **swCommands\_Save\_Template** | 921; valid for drawings, opens the Save Sheet Format dialog; **File menu > Save Sheet Format** |
| **swCommands\_Save\_To\_Webfolder** | 1680; saves an assembly to a web folder |
| **swCommands\_Save\_Virtual\_Comp** | 3464; performs an external save of a virtual component in an assembly; in the FeatureManager design tree, right click a virtual component and select **RMB menu > Save Part(In External file)** |
| **swCommands\_SaveAll** | 19; **Standard toolbar > Save** All |
| **swCommands\_SaveAs** | 620; **Standard toolbar > Save** **As** |
| **swCommands\_SaveBlock** | 473; valid for blocks created in assembly layouts; **Blocks toolbar** **> Save Sketch as Block** |
| **swCommands\_SaveLocally** | 3457; 3DEXPERIENCE SOLIDWORKS only, saves the active document to your cache; **File menu > Save Locally** |
| **swCommands\_Savenotification** | 2357; valid during autosave, sends the current window the save notification specifics |
| **swCommands\_Saveto\_Separate\_File** | 2375; valid for weldment cut-list items, opens the Insert Into New Part PropertyManager page; in the FeatureManager design tree, **Cut list folder >** *item* **RMB menu > Insert into New Part** |
| **swCommands\_SaveWithOptions** | 3456; 3DEXPERIENCE SOLIDWORKS only, opens a dialog of options with which to save the active document; **File menu > Save with Options...** |
| **swCommands\_ScaleEntities** | 504; valid for an open sketch, opens the Scale PropertyManager page; **Sketch toolbar > Scale Entities** |
| **swCommands\_ScanEqual** | 78; valid for drawings; **Dimensions/Relations toolbar > Scan Equal** |
| **swCommands\_ScanTo3D** | 622; **SOLIDWORKS Add-ins toolbar > ScanTo3D** |
| **swCommands\_Scene** | 2799; **View toolbar > Apply Scene** |
| **swCommands\_Schedule\_Render** | 2970; opens the Schedule Render dialog; **Render Tools toolbar > Schedule Render** |
| **swCommands\_ScreenCapture** | 604; **Screen Capture toolbar > Image Capture** |
| **swCommands\_ScreenCaptureAvi\_Begin** | 2814; opens the Record Screen Capture to File dialog; **Screen Capture toolbar > Record Video** |
| **swCommands\_ScreenCaptureAvi\_End** | 2815; valid if a screen is being videoed; **Screen Capture toolbar > Stop Video Record** |
| **swCommands\_ScreenCaptureToolbar** | 2813; alternative to swCommands\_Toolbar\_ScreenCapture; **View menu > Toolbars > Screen Capture** |
| **swCommands\_Search\_Detail\_Items** | 1998; accelerator F key to Find/Replace text in detail items |
| **swCommands\_SearchCommands** | 3019; **Help menu > Search > Commands** |
| **swCommands\_SearchFilesAndModels** | 3020; **Help menu > Search > Files and Models** |
| **swCommands\_SearchHelp** | 3016; **Help menu > Search > SOLIDWORKS Help** |
| **swCommands\_SearchManufacturers** | 3180; **Help menu > Search > Manufacturers** |
| **swCommands\_SearchMySolidworks** | 3174; **Help menu > Search > MySolidWorks** |
| **swCommands\_SecondaryAdvStructMember** | 3337; creates a secondary structural member feature by sweeping pre-defined profiles along user-defined planes; **Structures toolbar > Secondary Structural Member...** |
| **swCommands\_SectionProperties** | 383; opens the Section Properties dialog; **Tools toolbar > Section Properties** |
| **swCommands\_SectionView** | 124; opens the Section View PropertyManager page; **View toolbar > Section View** |
| **swCommands\_Segment** | 3129; valid for an open sketch, opens the Segment PropertyManager page; **Sketch toolbar > Segment** |
| **swCommands\_SegmentImportedMeshBody** | 3357; segments imported solid and surface mesh bodies; **Features toolbar > Segment Imported Mesh Body** |
| **swCommands\_Select\_All** | 634; dialog resource **Select All** |
| **swCommands\_Select\_Annotation\_View** | 3135; valid for 3D annotations; opens the Select annotation view dialog; in the graphics area, *dim* **RMB menu > Select Annotation View** |
| **swCommands\_Select\_Chain** | 2471; valid for an open sketch, in the graphics area, *selected\_line* **RMB menu > Select Chain** |
| **swCommands\_Select\_Display\_State** | 2808; **Display States toolbar > dropdown** |
| **swCommands\_Select\_Loop** | 1420; in the graphics area, *selected\_edge* **RMB menu > Select Loop** |
| **swCommands\_Select\_Midpoint** | 802; valid for specific dialogs, such as the Deform PropertyManager page; in the graphics area,**RMB menu > Select Midpoint**; also valid for *selected\_edge* **RMB menu > Select Midpoint** |
| **swCommands\_Select\_Open\_Edge\_Loop** | 1697; valid when the Untrim Surface PropertyManager page is open, and a surface edge is selected; in the graphics area, *surface\_edge* **RMB menu > Select Open Loop** |
| **swCommands\_Select\_Open\_Half\_Loop** | 2435; valid when the Surface-Untrim1 PropertyManager page is open, and a surface edge is selected; in the graphics area, *surface\_edge* **RMB menu > Select Partial Loop** |
| **swCommands\_Select\_Seed\_Feature** | 1802; valid for a selected pattern feature; in the graphics area, *sel\_pattern* **RMB menu > Select Seed of Pattern** |
| **swCommands\_Select\_Snapshot** | 3031; valid for assemblies, opens the Name Snapshot dialog; **View toolbar > Take Snapshot** |
| **swCommands\_Select\_SubAssembly\_In\_GraphicsView** | 2824; valid for a selected component of a subassembly; in the graphics area, *subasm\_comp* **RMB menu > Select Subassembly** |
| **swCommands\_Select\_Tangency** | 1428; valid when the Surface-Untrim1 PropertyManager page is open, and a surface edge is selected; in the graphics area, *surface\_edge* **RMB menu > Select Tangency** |
| **swCommands\_Select\_Tangency\_Laminar** | 1696; valid when the Surface-Untrim1 PropertyManager page is open, and a surface edge is selected; in the graphics area, *surface\_edge* **RMB menu > Select Open Tangency** |
| **swCommands\_SelectAllFilters** | 275; **Selection Filter toolbar > Select All Filters** |
| **swCommands\_SelectConfigurations** | 3116; **Configurations toolbar > dropdown** |
| **swCommands\_SelectionFilters** | 486; alternative to swCommands\_New\_Toolbar\_Sel\_Filter; **View menu > Toolbars > Selection Filter** |
| **swCommands\_Selective\_Open** | 3033; valid for a selected assembly opened in Large Design Review mode, opens the Selective Open dialog; in the FeatureManager design tree, *top\_assy* **RMB menu > Selective Open** |
| **swCommands\_Selective\_Open\_LightWeight** | 3038; valid for a selected assembly opened in Large Design Review mode, opens the Selective Open in Lightweight dialog; in the FeatureManager design tree, *top\_assy* **RMB menu > Selective Open in Lightweight** |
| **swCommands\_SelectOverGeometry** | 3310; VIRTKEY "T"; enables/disables box and lasso selection to start on faces; **Standard toolbar > Select over Geometry** |
| **swCommands\_SendTo** | 3045; **File menu > Send To** |
| **swCommands\_Set\_As\_Anchor** | 1624; valid for a selected point in a drawing sheet whose format is in edit mode; *sketch\_pt* **RMB menu > Set as Anchor >** *table\_type* |
| **swCommands\_Set\_Current\_View\_As\_Back** | 3085; valid for assemblies and parts; **View menu > Modify > Set Current View As > Back** |
| **swCommands\_Set\_Current\_View\_As\_Bottom** | 3087; valid for assemblies and parts; **View menu > Modify > Set Current View As > Bottom** |
| **swCommands\_Set\_Current\_View\_As\_Front** | 3084; valid for assemblies and parts; **View menu > Modify > Set Current View As > Front** |
| **swCommands\_Set\_Current\_View\_As\_Left** | 3089; valid for assemblies and parts; **View menu > Modify > Set Current View As > Left** |
| **swCommands\_Set\_Current\_View\_As\_Right** | 3088; valid for assemblies and parts; **View menu > Modify > Set Current View As > Right** |
| **swCommands\_Set\_Current\_View\_As\_Top** | 3086; valid for assemblies and parts; **View menu > Modify > Set Current View As > Top** |
| **swCommands\_Set\_Dim\_Extension\_Centerline** | 3106; valid for a drawing with a dimension extension line; in the graphics area, *dim\_ext\_line* **RMB menu > Set Extension Line as Centerline** |
| **swCommands\_Set\_QuickView\_Transparency** | 3032; valid for assemblies opened in Large Design Review mode with one or more modified components; **View toolbar > Filter Modified Components** |
| **swCommands\_Shaded** | 337; **View toolbar > Display Style > Shaded** |
| **swCommands\_ShadedSketchContours** | 3189; **Sketch toolbar > Shaded Sketch Contours** |
| **swCommands\_ShadedWithEdges** | 506; **View toolbar > Display Style > Shaded With Edges** |
| **swCommands\_ShadowsInShadedMode** | 399; valid for parts and assemblies; **View toolbar > View Settings > Shadows in Shaded Mode** |
| **swCommands\_Share** | 3524; opens a Share dialog to share a copy of the current model with members outside or inside your organization; **File > Share** |
| **swCommands\_Share\_A\_File** | 3516; opens Share *file\_name\_with\_extension* dialog; **Tools > Lifecycle and Collaboration > Share a file** |
| **swCommands\_Sheet\_Tab\_Popup\_Activate** | 950; valid for drawings with a selected sheet tab; *sheet\_tab* **RMB menu > Activate** |
| **swCommands\_Sheet\_Tab\_Popup\_Add** | 948; valid for drawings with a selected sheet tab; *sheet\_tab* **RMB menu > Add Sheet** |
| **swCommands\_Sheet\_Tab\_Popup\_Delete** | 949; valid for drawings with a selected sheet tab; *sheet\_tab* **RMB menu > Delete** |
| **swCommands\_Sheet\_Tab\_Popup\_Properties** | 947; valid for drawings with a selected sheet tab; *sheet\_tab* **RMB menu > Properties** |
| **swCommands\_Sheet\_Tab\_Popup\_Rename** | 2717; valid for drawings with a selected sheet tab; *sheet\_tab* **RMB menu > Rename** |
| **swCommands\_SheetMetal** | 487; alternative to swCommands\_Toolbar\_Sht\_Mtl; **View menu > Toolbars > Sheet Metal** |
| **swCommands\_SheetmetalCosting** | 3006; **Tools toolbar > Costing** |
| **swCommands\_Shell** | 32; valid for parts with a selected sketch; **Features toolbar > Shell** |
| **swCommands\_Show\_3d\_Sketch\_Triad** | 2440; valid for an open 3D sketch; in the graphics area, **RMB menu > Show Sketcher Triad** |
| **swCommands\_Show\_Ann\_Based\_Swift\_Tree** | 2086; valid for a selected scheme in DimXpertManager; in the DimXpertManager, *sel\_scheme* **RMB menu > Tree Display > Show annotation based tree** |
| **swCommands\_Show\_Bom** | 1240; valid for a drawing view with an Excel-based BOM; *excel\_based\_bom* **RMB menu > Show** |
| **swCommands\_Show\_CADFamily\_Name** | 3461; 3DEXPERIENCE SOLIDWORKS assemblies only, displays the CAD family in which the part reference belongs in the FeatureManager design tree; **FeatureManager design tree > Top Assembly RMB menu > Tree Display > Show CAD Family Name** |
| **swCommands\_Show\_Comp\_Des** | 2490; valid for a selected top-level assembly; in the FeatureManager design tree, *top\_asm* **RMB menu > Tree Display > Show Component Descriptions** |
| **swCommands\_Show\_Comp\_Filename** | 2489; valid for a selected top-level assembly; in the FeatureManager design tree, *top\_asm* **RMB menu > Tree Display > Show Component Names** |
| **swCommands\_Show\_ComponentInstance\_Name** | 3458; 3DEXPERIENCE SOLIDWORKS assemblies only, displays the full name derived from the component's properties in the FeatureManager design tree; **FeatureManager design tree > Top Assembly RMB menu > Tree Display > Show Component Instance Name** |
| **swCommands\_Show\_ComponentReference\_Name** | 3459; 3DEXPERIENCE SOLIDWORKS assemblies only, displays the Family Name (physical product) of the part being referenced in the FeatureManager design tree; **FeatureManager design tree > Top Assembly RMB menu > Tree Display > Show Component ReferenceName** |
| **swCommands\_Show\_Components** | 926; valid for selected components in assemblies; in the FeatureManager design tree, *selected\_comp* **RMB context toolbar > Show Components** |
| **swCommands\_Show\_Components\_All\_Configs** | 1651; valid for a selected top-level assembly; **Edit menu > Show > All Display States** |
| **swCommands\_Show\_Components\_Select\_Configs** | 1652; valid for a selected top-level assembly, opens the Apply To Display States dialog; **Edit menu > Show > Specified Display States** |
| **swCommands\_Show\_Config\_Description** | 2511; valid for a selected top-level assembly; in the FeatureManager design tree, *top\_asm* **RMB menu > Tree Display > Show Component Configuration Descriptions** |
| **swCommands\_Show\_Config\_Name** | 2491; valid for a selected top-level assembly; in the FeatureManager design tree, *top\_asm* **RMB menu > Tree Display > Show Component Configuration Names** |
| **swCommands\_Show\_Config\_Or\_DisplayState\_Name** | 3199; valid for a selected top-level assembly; in the FeatureManager design tree, *top\_asm* **RMB menu > Tree Display > Show Configuration/Display State Names if at least one exists** |
| **swCommands\_Show\_Config\_Previews** | 2494; valid for a selected configuration; in the ConfigurationManager, *config* **RMB menu > Show Preview** |
| **swCommands\_Show\_Configdes\_In\_Configtree** | 2493; valid for assemblies; in ConfigurationManager, *top\_level\_config* **RMB menu > Tree Display > Show Configuration Descriptions** |
| **swCommands\_Show\_Configname\_In\_Configtree** | 2492; valid for assemblies; in ConfigurationManager, *top\_level\_config* **RMB menu > Tree Display > Show Configuration Names** |
| **swCommands\_Show\_Configuration** | 1535; valid for a selected inactive configuration, in ConfigurationManager, *inactive\_config* **RMB menu > Show Configuration** |
| **swCommands\_Show\_Configuration\_Adv** | 1558; valid for assemblies, opens the Advanced Show/Hide Components dialog |
| **swCommands\_Show\_Cthread** | 1529; valid for a model with a hidden, selected cosmetic thread; in the FeatureManager design tree, *cosmetic\_thread* **RMB context toolbar > Show Cosmetic Thread** |
| **swCommands\_Show\_Dependents** | 1046; valid for a selected top-level assembly; **Edit Menu > Show with Dependents > Current Display State** |
| **swCommands\_Show\_Dependents\_All\_Configs** | 1647; valid for a selected top-level assembly; **Edit Menu > Show with Dependents > All Display States** |
| **swCommands\_Show\_Dependents\_Select\_Configs** | 1648; valid for a selected top-level assembly; **Edit Menu > Show with Dependents > Specified Display States** |
| **swCommands\_Show\_Dim** | 1540; use swCommands\_HideShowAnnotations to display hidden annotations |
| **swCommands\_Show\_Dim\_Align** | 1564; valid for a selected drawing dimension to which Align Collinear/Radial has been applied; in the graphics area, *aligned\_dim* **RMB menu > Show Alignment** |
| **swCommands\_Show\_Dim\_Leader** | 2539; valid for a drawing with a selected dimension with a hidden leader line; *leader\_line* **RMB menu > Show Dimension Lines** |
| **swCommands\_Show\_Dim\_Witness** | 2527; valid for a drawing with a selected dimension with a hidden witness line; *witness\_line* **RMB menu > Show Extension Lines** |
| **swCommands\_Show\_Explode\_Steps** | 1556; valid for a selected component in an assembly with an Exploded View; in the FeatureManager design tree, *component* **RMB menu > Show Explode Steps** |
| **swCommands\_Show\_Feat\_Based\_Swift\_Tree** | 2085; valid for a selected scheme in DimXpertManager; in the DimXpertManager, *sel\_scheme* **RMB menu > Tree Display > Show feat based tree** |
| **swCommands\_Show\_Feature\_Des** | 2488; valid for a selected top-level assembly; in the FeatureManager design tree, *top\_asm* **RMB menu > Tree Display > Show Feature Descriptions** |
| **swCommands\_Show\_Feature\_Detail** | 927; valid for a selected top-level assembly showing hierarchy only; in the graphics area, **RMB menu > Show Feature Detail** |
| **swCommands\_Show\_Feature\_History** | 2599; valid for a part with a selected solid or surface body folder; *sel\_folder* **RMB menu > Show Feature History** |
| **swCommands\_Show\_Feature\_Name** | 2487; valid for a selected top-level assembly; in the FeatureManager design tree, *top\_asm* **RMB menu > Tree Display > Show Feature Names** |
| **swCommands\_Show\_Flat\_Swift\_Tree** | 2087; valid for a selected scheme in DimXpertManager; in the DimXpertManager, *sel\_scheme* **RMB menu > Tree Display > Show flat tree** |
| **swCommands\_Show\_Hidden\_comps** | 2810; valid for assemblies, opens the Show Hidden dialog; **Assembly toolbar > Show Hidden Components** |
| **swCommands\_Show\_Hidden\_comps\_Exit** | 3022; dialog resource **Cancel** |
| **swCommands\_Show\_Hidden\_comps\_Undo** | 3021; dialog resource **Undo** |
| **swCommands\_Show\_Hide\_Fixed\_Length\_Route\_Manipulators** | 3150; valid for the SOLIDWORKS Routing add-in and an open assembly with a route and selected route segments; **Routing Tools toolbar > Show Fixed Length Dimensions** |
| **swCommands\_Show\_Incontext\_Feature\_Holders** | 686; valid for a selected top-level assembly with hidden update holders; *selected\_assembly* **RMB menu > Show Update Holders** |
| **swCommands\_Show\_LDR\_Configuration** | 3203; valid for assemblies opened in Large Design Review mode for a selected configuration in ConfigurationManager; in the ConfigurationManager, *hidden\_config* **RMB menu > Show Configuration** |
| **swCommands\_Show\_Mate\_Component\_1** | 2530; valid for assemblies with hidden mate components; in the FeatureManager design tree, *first\_part\_mate\_constraint* **RMB menu >** *second\_part\_mate* **> Show component** |
| **swCommands\_Show\_Mate\_Component\_2** | 2535; valid for assemblies with hidden mate components; in the FeatureManager design tree, second*\_part\_mate\_constraint* **RMB menu >** *first\_part\_mate* **> Show component** |
| **swCommands\_Show\_Mesh\_Feat** | 3210; valid for a selected mesh feature that is hidden; **RMB menu > Show** |
| **swCommands\_Show\_Representation\_Name** | 3460; 3DEXPERIENCE SOLIDWORKS assemblies only, displays the representation name of the part in the FeatureManager design tree; **FeatureManager design tree > Top Assembly RMB menu > Tree Display > Show Component Reference Representation Name** |
| **swCommands\_Show\_Revision\_And\_Maturity** | 3462; 3DEXPERIENCE SOLIDWORKS assemblies only, displays a component's revisions and maturity in the FeatureManager design tree; **FeatureManager design tree > Top Assembly RMB menu > Tree Display > Show Revision and Maturity** |
| **swCommands\_Show\_Sketch\_Dim\_In\_Drawing** | 2479; valid for a selected hidden dimension in a drawing sketch; **RMB menu > Show Dimensions** |
| **swCommands\_Show\_Table** | 2622; valid for models with hidden tables; in the FeatureManager design tree, *table\_name* **RMB menu > Show Table** |
| **swCommands\_Show\_Triad\_Manipulator** | 769; valid for a selected component in an assembly, displays the triad manipulator |
| **swCommands\_Show\_View\_Palette** | 2243; valid for drawings; accelerator key P to display view palette |
| **swCommands\_Show\_Zone** | 1560; valid for assemblies with envelope components; in the FeatureManager design tree, *envelope\_feature* **RMB menu > Envelope > Show/Hide Using Envelope** |
| **swCommands\_ShowCurvatureCombs** | 4; valid for a selected spline, opens the Curvature Scale PropertyManager page; **Spline Tools toolbar > Show Curvature Combs** |
| **swCommands\_ShowEdge** | 352; valid for drawings, opens the Show Edge PropertyManager page |
| **swCommands\_ShowGuidelines** | 2983; valid for the SOLIDWORKS Routing add-in for an open assembly route; **Routing Tools toolbar > Show Guidelines** |
| **swCommands\_ShowInflectionPoints** | 417; valid for an open sketch of a selected spline, opens the Spline PropertyManager page; **Spline Tools toolbar > Show Inflection Points** |
| **swCommands\_ShowMinimumRadius** | 418; valid for an open sketch of a selected spline, opens the Spline PropertyManager page; **Spline Tools toolbar > Show Minimum Radius** |
| **swCommands\_ShowSplineHandles** | 443; valid for an open sketch of a selected spline; **Spline Tools toolbar > Show Spline Handles** |
| **swCommands\_ShutOffSurfaces** | 452; valid for parts; **Mold Tools toolbar > Shut-off Surfaces** |
| **swCommands\_SimElementOff** | 2829; valid only in the context of a Motion Study gantt chart for a selected simulation element row; in the gantt chart, *rotary\_motor\_bar* **RMB menu > Off** |
| **swCommands\_SimElementOn** | 2828; valid only in the context of a Motion Study gantt chart for a selected simulation element row; in the gantt chart, *rotary\_motor\_bar* **RMB menu > On** |
| **swCommands\_SimElementSuppress** | 2830; valid only in the context of a Motion Study gantt chart for a selected simulation element row; in the MotionManager design tree, *rotary\_motor\_bar* **RMB menu > Suppress** |
| **swCommands\_SimElementUnsuppress** | 2831; valid only in the context of a Motion Study gantt chart for a selected, suppressed simulation element row; in the MotionManager design tree, *rotary\_motor\_bar* **RMB menu > Unsuppress** |
| **swCommands\_SimpleHole** | 12; valid for sheet metal parts; **Sheet Metal toolbar > Simple Hole** |
| **swCommands\_SimplifySpline** | 144; valid for a selected spline in an open sketch; **Spline Tools toolbar > Simplify Spline** |
| **swCommands\_SimulationDesigner** | 3527; SOLIDWORKS Connected only; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Simulation Designer** |
| **swCommands\_SimulationPremium** | 3435; valid only if entitled; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Simulation Premium** |
| **swCommands\_SimulationPro** | 3434; valid only if entitled; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Simulation Professional** |
| **swCommands\_SimulationStd** | 3433; valid only if entitled; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Simulation Standard** |
| **swCommands\_SingleView** | 549; **View toolbar > View Orientation > Single View** |
| **swCommands\_Sk\_Close\_Contour** | 1048; valid for a selected open profile in an open sketch; **Tools menu > Sketch Tools > Close Sketch to Model** |
| **swCommands\_Sk\_Endchain** | 1674; valid during insertion of an arc or line in an open sketch; in the graphics area, *sketch\_line* **RMB menu > End chain (double-click)** |
| **swCommands\_Sk\_Endcos** | 2126; valid for an open sketch duirng spline on surface creation, stops the drawing of the spline and opens the Spline PropertyManager page |
| **swCommands\_Sk\_Endspline** | 1804; valid for an open sketch duirng spline creation, stops the drawing of the spline and opens the Spline PropertyManager page |
| **swCommands\_Sketch** | 45; valid for a selected plane or sketch; **Sketch toolbar > Sketch** |
| **swCommands\_Sketch\_Align\_Grid\_Origin** | 2727; valid for an open sketch, opens the Align Grid/Origin PropertyManager page; **Tools > Sketch Tools > Align > Align Grid/Origin** |
| **swCommands\_Sketch\_Detach** | 1547; valid for an open sketch; **Sketch toolbar > Detach Segment On Drag** |
| **swCommands\_Sketch\_Jog\_Flip** | 1817; valid for a sketch jog line in an assembly view; **RMB menu > Flip Direction** |
| **swCommands\_Sketch\_Suppress\_Constraints** | 1936; valid for a selected sketch relations manipulator; in the graphics area, *manip* **RMB menu > Toggle Suppression** |
| **swCommands\_SketchChamfer** | 358; valid for an open sketch, opens the Sketch Chamfer PropertyManager page; **Sketch toolbar > Sketch Chamfer** |
| **swCommands\_SketchCreateChain** | 617; valid when inserting a Grid System, opens the Path PropertyManager page; in the graphics area, **RMB menu > Make Path** |
| **swCommands\_SketchDrivenPattern** | 304; valid for parts with a selected sketch; **Features toolbar > Sketch Driven Pattern** |
| **swCommands\_SketchedBend** | 323; valid for sheet metal parts; **Sheet Metal toolbar > Sketched Bend** |
| **swCommands\_SketchFillet** | 62; valid for an open sketch, opens the Sketch Fillet PropertyManager page; **Sketch toolbar > Sketch Fillet** |
| **swCommands\_SketchGroupRebuild** | 555; valid for an open sketch block; **Blocks toolbar > Rebuild** |
| **swCommands\_SketchPicture** | 368; opens the Open dialog; **Sketch toolbar > Sketch Picture** |
| **swCommands\_Sketchplane\_Delete** | 2681; valid for a selected sketch plane in the 3D sketch environment; **RMB menu > Delete** |
| **swCommands\_Sketchplane\_Deleteall** | 2682; valid for a selected sketch plane in the 3D sketch environment; **RMB menu > Delete all** |
| **swCommands\_Sketchplane\_Rename** | 2683; valid for a selected sketch plane in the 3D sketch environment; **RMB menu > Rename** |
| **swCommands\_SketchSlicing** | 3399; opens the Slicing PropertyManager; **Insert menu > Slicing** or **Sketch toolbar > Slicing** |
| **swCommands\_SketchSlot\_Arc\_Center** | 2867; valid for a selected plane, planar face, or edge, opens the Slot PropertyManager page; **Sketch toolbar > Centerpoint Arc Slot** |
| **swCommands\_SketchSlot\_Arc3P** | 2866; valid for a selected plane, planar face, or edge, opens the Slot PropertyManager page; **Sketch toolbar > 3 Point Arc Slot** |
| **swCommands\_SketchSlot\_Line** | 2864; valid for a selected plane, planar face, or edge, opens the Slot PropertyManager page; **Sketch toolbar > Straight Slot** |
| **swCommands\_SketchSlot\_Line\_Center** | 2865; valid for a selected plane, planar face, or edge, opens the Slot PropertyManager page; **Sketch toolbar > Centerpoint Straight Slot** |
| **swCommands\_SketchToolbar** | 489; alternative to swCommands\_Toolbar\_Sketch; **View menu > Toolbars > Sketch** |
| **swCommands\_Skey\_SearchBox** | 3471; Opens a command search box; in the graphics area, click "s" or select **Help menu > Search > Commands** |
| **swCommands\_Skg\_Cancel** | 2027; valid during block creation, cancels |
| **swCommands\_Skg\_Ok** | 2026; valid during a block edit; **RMB menu > Exit Block Edit** |
| **swCommands\_Skg\_Remove** | 2023; removes a selected sketch block |
| **swCommands\_SkSilhouetteEnts** | 3414; converts silhouette outlines of bodies and components into sketch segments; **Sketch toolbar > Silhouette Entities** |
| **swCommands\_Sktools\_Autoconstr** | 987; valid for an open, unconstrained sketch; **Tools menu > Relations> Constrain All Relations** |
| **swCommands\_Sm\_Clear\_Problem\_Areas** | 2945; valid for a sheet metal flat pattern feature with problem areas; in the graphics area, **RMB menu > Clear problem areas** |
| **swCommands\_Sm\_Convert\_To\_Sheetmetal** | 2245; converts a part to a sheet metal part |
| **swCommands\_Sm\_Measure\_Bend\_Deviation** | 1830; valid for a selected sheet metal bend feature; in the FeatureManager design tree, *bend* **RMB menu > Bend Deviation** |
| **swCommands\_Sm\_Reorder\_Bends** | 1096; valid for a selected sheet metal bend feature; in the FeatureManager design tree, *bend* **RMB menu > Reorder Bends** |
| **swCommands\_Sm\_Show\_Problem\_Areas** | 2944; valid for a selected sheet metal flat pattern feature with cleared problem areas; in the graphics area, **RMB menu > Show problem areas** |
| **swCommands\_Sm\_Toggle\_Flat\_Display** | 2924; valid for a selected flat pattern feature of a sheet metal part; in the graphics area, **RMB menu > Toggle flat display** |
| **swCommands\_Small\_Icon** | 1621; valid in the Appearances, Scenes, and Decals task pane palette; *palette* **RMB menu > Small Icons** |
| **swCommands\_Small\_List\_Icon** | 2064; valid in content list popups; **RMB menu > List, Small Icons** |
| **swCommands\_Smart\_Feature\_Preview** | 2218; valid for assemblies with a selected smart feature component; in the FeatureManager design tree, **History folder >** *smart\_component* **> Smart Feature folder > Components >** *comp* **RMB menu > Preview** |
| **swCommands\_Smart\_Mate** | 1343; valid for assemblies, opens the SmartMates PropertyManager page; **Assembly toolbar > SmartMates** |
| **swCommands\_SmartDimension** | 38; opens the Dimension PropertyManager page; **Layout Tools** or **Dimensions/Relations toolbar > Smart Dimension** |
| **swCommands\_SmartFasteners** | 7; valid for assemblies, opens the Smart Fasteners PropertyManager page; **Assembly toolbar > Smart Fasteners** |
| **swCommands\_Smc\_Help** | 2219; valid for a Smart Component as it is being edited in its defining assembly, opens the Editing Definition of a Smart Component topic in the SOLIDWORKS help; **SMC popup toolbar > Help** |
| **swCommands\_SMGusset** | 3111; valid for sheet metal parts, opens the Sheet Metal Gusset PropertyManager page; **Sheet Metal toolbar > Sheet Metal Gusset** |
| **swCommands\_SMNormalCut** | 3196; opens the Normal Cut PropertyManager page; **Sheet Metal toolbar > Normal Cut** |
| **swCommands\_SmoothMesh** | 3469; Opens the Smooth Graphics Mesh PropertyManager for a selected graphics body or facet group; **Insert menu > Mesh > Mesh Smoothing** |
| **swCommands\_SMStamp** | 3518; Inserts a sheet metal stamp; **Insert menu > Sheet Metal > Stamp** |
| **swCommands\_Snap\_To\_Selection** | 2275; valid after *component* **RMB menu > Move with Triad** command in assembly; in the graphics area, *triad\_center\_ball* **RMB menu > Move to selection** |
| **swCommands\_Snap\_While\_Dragging** | 2276; valid for a selected Move with Triad ring in an assembly; *triad\_ring* **RMB menu > Snap while dragging** |
| **swCommands\_Solid\_Data\_Manager** | 1393; valid if SOLIDWORKS Explorer is installed; **Tools menu > SOLIDWORKS Applications > SOLIDWORKS Explorer** |
| **swCommands\_SolidToSheetMetal** | 2882; valid for sheet metal parts; **Sheet Metal toolbar > Convert to Sheet Metal** |
| **swCommands\_SolidWorks\_backoffice** | 3356; **Tools menu > SOLIDWORKS Applications > SOLIDWORKS Task Scheduler...** |
| **swCommands\_SolidworksAnimator** | 433; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Animator** |
| **swCommands\_SolidworksOffice** | 491; alternative to swCommands\_Toolbar\_Office; **View menu > Toolbars > SOLIDWORKS Add-ins** |
| **swCommands\_SolidworksRouting** | 566; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Routing** |
| **swCommands\_SolidworksToolbox** | 437; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Toolbox** |
| **swCommands\_SolidworksUtilities** | 436; **SOLIDWORKS Add-ins toolbar > SOLIDWORKS Utilities** |
| **swCommands\_SolveAsFlexibleOrRigid** | 3095; valid for a selected subassembly; **Assembly toolbar > Make Subassembly Flexible** |
| **swCommands\_Sort\_Stacked\_Balloons** | 3161; valid for a selected annotation with stacked balloons; in the graphics area, *stacked\_balloon\_anno* **RMB menu > Sort Stacked Balloons** |
| **swCommands\_SpaceEvenlyAcross** | 312; valid for multi-selected annotations or dimensions; **Align toolbar > Space Evenly Across** |
| **swCommands\_SpaceEvenlyDown** | 313; valid for multi-selected annotations or dimensions; **Align toolbar > Space Evenly Down** |
| **swCommands\_SpaceTightlyAcross** | 316; valid for multi-selected annotations or dimensions; **Align toolbar > Space Tightly Across** |
| **swCommands\_SpaceTightlyDown** | 317; valid for multi-selected annotations or dimensions; **Align toolbar > Space Tightly Down** |
| **swCommands\_SpellChecker** | 535; opens the Spelling Check PropertyManager page; **Tools toolbar > Spell Checker** |
| **swCommands\_Spline** | 47; valid for a selected plane or planar face; **Sketch toolbar > Spline** |
| **swCommands\_SplineOnSurface** | 542; valid for a selected face or surface; **Sketch toolbar > Spline on Surface** |
| **swCommands\_Splines** | 492; alternative to swCommands\_Toolbar\_Spline\_Tools; **View menu > Toolbars > Spline Tools** |
| **swCommands\_Split\_Open\_Route** | 2342; valid for the SOLIDWORKS Routing add-in; splits an open route for selected splittable segments |
| **swCommands\_Split\_Open\_Segm\_Ar** | 1858; valid for the SOLIDWORKS Routing Add-in and when the Auto Route PropertyManager page is open; in the graphics area, **RMB menu > Split Entity** |
| **swCommands\_Split\_Route** | 2269; valid for the SOLIDWORKS Routing add-in and an open routing assembly; **Routing Tools toolbar > Split Route** |
| **swCommands\_SplitEntities** | 293; valid for an open sketch and a selected sketch entity; **Sketch toolbar > Split Entities** |
| **swCommands\_Spool\_Command** | 3013; valid for the SOLIDWORKS Routing add-in and an open piping route, opens the Spools PropertyManager page; **Piping toolbar > Define Spools** |
| **swCommands\_Spool\_Tube\_Command** | 3044; valid for SOLIDWORKS Routing add-in and an open flexible tube assembly; in the graphics area, *sel\_route\_or\_tube\_comp* **RMB menu > Define Spools** |
| **swCommands\_Stack** | 534; valid for selected text; **Formatting toolbar > Stack** |
| **swCommands\_Stack\_Dir\_Down** | 678; valid for a selected stacked balloon stacked left, right, or up; in the graphics area, *stacked\_balloon* **RMB menu > Down** |
| **swCommands\_Stack\_Dir\_Left** | 680; valid for a selected stacked balloon stacked down, right, or up; in the graphics area, *stacked\_balloon* **RMB menu > Left** |
| **swCommands\_Stack\_Dir\_Right** | 681; valid for a selected stacked balloon stacked left, down, or up; in the graphics area, *stacked\_balloon* **RMB menu > Right** |
| **swCommands\_Stack\_Dir\_Up** | 677; valid for a selected stacked balloon stacked left, right, or down; in the graphics area, *stacked\_balloon* **RMB menu > Up** |
| **swCommands\_StackedBalloons** | 319; opens the Stacked Balloon PropertyManager page; **Annotation toolbar > Stacked Balloons** |
| **swCommands\_StackFasteners** | 3410; valid for assemblies, adds a fastener stack to the asembly using the SOLIDWORKS Toolbox library of standard hardware; **Assembly toolbar > Fastener Stack** |
| **swCommands\_Standard** | 493; alternative to swCommands\_Toolbar\_Standard; **View menu > Toolbars > Standard** |
| **swCommands\_Standard3View** | 42; **Drawing toolbar > Standard 3 View** |
| **swCommands\_StandardViews** | 494; alternative to swCommands\_Toolbar\_Stdview; **View menu > Toolbars > Standard Views** |
| **swCommands\_Start\_Contour\_Single\_Select** | 660; valid for parts or assemblies, starts contour single select mode |
| **swCommands\_Start\_Screen** | 3229; opens the Welcome dialog; CTRL-F2; **Standard toolbar > Welcome to SOLIDWORKS** |
| **swCommands\_Start\_Select\_Contour** | 2495; valid for a selected sketch contour; *sketch\_contour* **RMB menu > Contour Select Tool** |
| **swCommands\_Start\_Select\_Contour\_2** | 2514; valid when the Planar Surface PropertyManager page is open, and the planar surface sketch is selected; in the graphics area, *planar\_surface\_sketch* **RMB menu > Start Contour Selection** |
| **swCommands\_Start\_Smart\_Selection** | 2628; valid when a PropertyManager page supporting multi-edge selection is open; in the graphics area, *sel\_edge* **RMB menu > Start/Edit Smart Selection** |
| **swCommands\_Statistics** | 427; valid for parts and drawings; **Tools toolbar > Performance Evaluation** |
| **swCommands\_StopCurrentJump** | 129; **Web toolbar > Stop Current Jump** |
| **swCommands\_StopMacro** | 31; valid for a running macro, opens the Save As dialog; **Macro toolbar > Stop Macro** |
| **swCommands\_StretchEntities** | 2851; valid for an open sketch, opens the Stretch PropertyManager page; **Sketch toolbar > Stretch Entities** |
| **swCommands\_Strikeout** | 532; valid for selected text; **Formatting toolbar > StrikeOut** |
| **swCommands\_StructuralMember** | 465; valid for weldments, opens the Structural Member PropertyManager page; **Weldments toolbar > Structural Member** |
| **swCommands\_Submit** | 794; dialog resource **Submit** |
| **swCommands\_Suppress** | 14; valid for one or more selected features; **Edit menu > Suppress > This Configuration** |
| **swCommands\_Suppress\_Mate\_Component\_1** | 2531; valid for assemblies with visible, resolved mate components; in the FeatureManager design tree, *first\_part\_mate\_constraint* **RMB menu >** *second\_part\_mate* **>** **Suppress component** |
| **swCommands\_Suppress\_Mate\_Component\_2** | 2536; valid for assemblies with visible, resolved mate components; in the FeatureManager design tree, *second\_part\_mate\_constraint* **RMB menu >** *first\_part\_mate* **> Suppress Component** |
| **swCommands\_Surface\_Flatten** | 3139; opens the Flatten PropertyManager page; **Surfaces toolbar > Surface Flatten** |
| **swCommands\_SurfaceFinish** | 112; opens the Surface Finish PropertyManager page; **Annotation toolbar > Surface Finish** |
| **swCommands\_Surfaces** | 495; alternative to swCommands\_Toolbar\_Surface; **View menu > Toolbars > Surfaces** |
| **swCommands\_SurfFromMesh** | 3218; creates surfaces from mesh; **Mold or Surface toolbar > Surface From Mesh** |
| **swCommands\_Sw\_Animatorpane** | 2811; valid for assemblies; **View menu > Toolbars > MotionManager** |
| **swCommands\_Sw\_Beta\_Report** | 1412; opens the SOLIDWORKS Beta problem report from [www.solidworks.com](http://www.solidworks.com), if available |
| **swCommands\_Sw\_Educator\_Resources** | 3465; Opens www.solidworks.com/eduwhatsnew |
| **swCommands\_Sw\_Release\_Notes** | 1411; opens the Administration Guides from [www.solidworks.com](http://www.solidworks.com); **Help menu > Release Notes** |
| **swCommands\_Sw\_Taskpane** | 2127; **View menu > User Interface > Task Pane** |
| **swCommands\_SwConnected\_Release\_Notes** | 3500; displays the release notes for the installed version of SOLIDWORKS Connected; **SOLIDWORKS menu > Help > Release Notes > SOLIDWORKS Connected** *yyyy***x** |
| **swCommands\_SweptBossBase** | 64; valid for parts with a selected sketch; **Features toolbar > Swept Boss/Base** |
| **swCommands\_SweptCut** | 65; valid for parts with a selected sketch; **Features toolbar > Swept Cut** |
| **swCommands\_SweptFlange** | 3041; valid for sheet metal parts, opens the Swept Flange PropertyManager page; **Sheet Metal toolbar > Swept Flange** |
| **swCommands\_SweptSurface** | 103; opens the Surface-Sweep PropertyManager page; **Surfaces toolbar > Swept Surface** |
| **swCommands\_Swift\_Create\_Basic\_Dim** | 2780; valid for DimXpertManager and a selected Position tolerance; in the DimXpertManager, *position\_tol* **RMB menu > Recreate basic dim** |
| **swCommands\_Swift\_Fpo\_Boss** | 2755; **DimXpert feature selector > Boss** |
| **swCommands\_Swift\_Fpo\_Chamfer** | 2754; **DimXpert feature selector > Chamfer** |
| **swCommands\_Swift\_Fpo\_Compound** | 2665; **DimXpert feature selector > Compound Hole** |
| **swCommands\_Swift\_Fpo\_Cone** | 2669; **DimXpert feature selector > Cone** |
| **swCommands\_Swift\_Fpo\_Constr\_Circle** | 2283; **DimXpert feature selector > Intersect Circle** |
| **swCommands\_Swift\_Fpo\_Constr\_Line** | 2282; **DimXpert feature selector > Intersect Line** |
| **swCommands\_Swift\_Fpo\_Constr\_Plane** | 2284; **DimXpert feature selector > Intersect Plane** |
| **swCommands\_Swift\_Fpo\_Constr\_Point** | 2281; **DimXpert feature selector > Intersect Point** |
| **swCommands\_Swift\_Fpo\_Contersink** | 2667; **DimXpert feature selector > Countersink** |
| **swCommands\_Swift\_Fpo\_Counterbore** | 2666; **DimXpert feature selector > Counterbore** |
| **swCommands\_Swift\_Fpo\_Cylinder** | 2670; **DimXpert feature selector > Cylinder** |
| **swCommands\_Swift\_Fpo\_DimType\_Angular** | 2940; **DimXpert feature selector > Angular Dimension** |
| **swCommands\_Swift\_Fpo\_DimType\_Linear** | 2939; **DimXpert feature selector > Linear Dimension** |
| **swCommands\_Swift\_Fpo\_Fillet** | 2753; **DimXpert feature selector > Fillet** |
| **swCommands\_Swift\_Fpo\_Hole** | 2664; **DimXpert feature selector > Hole** |
| **swCommands\_Swift\_Fpo\_Notch** | 2752; **DimXpert feature selector > Notch** |
| **swCommands\_Swift\_Fpo\_Ok** | 2676; **DimXpert feature selector > OK** |
| **swCommands\_Swift\_Fpo\_Pattern** | 2675; **DimXpert feature selector > Pattern** |
| **swCommands\_Swift\_Fpo\_Plane** | 2663; **DimXpert feature selector > Plane** |
| **swCommands\_Swift\_Fpo\_Pocket** | 2674; **DimXpert feature selector > Pocket** |
| **swCommands\_Swift\_Fpo\_Slot** | 2672; **DimXpert feature selector > Slot** |
| **swCommands\_Swift\_Fpo\_Sphere** | 2671; **DimXpert feature selector > Sphere** |
| **swCommands\_Swift\_Fpo\_Surf** | 2662; **DimXpert feature selector > Surface** |
| **swCommands\_Swift\_Fpo\_Width** | 2673; **DimXpert feature selector > Width** |
| **swCommands\_SwiftAddTaStudy** | 2801; valid for SOLIDWORKS Premium assemblies whose parts have been assigned dimensions and tolerances; **DimXpert toolbar > TolAnalystStudy** |
| **swCommands\_SwiftDeleteAll** | 596; valid for parts with assigned tolerances; **DimXpert toolbar > Delete All Tolerances** |
| **swCommands\_SwiftInsertAngleDimension** | 3467; Adds a DimXpert angle dimension from the DimXPertManager tab; **Tools menu > MBD Dimension > Angle Dimension...** |
| **swCommands\_SwiftInsertBasicDimension** | 3182; valid for parts; **DimXpert toolbar > Basic Dimension** |
| **swCommands\_SwiftInsertBasicSizeDimension** | 3197; valid for parts; **DimXpert toolbar > Basic Size Dimension** |
| **swCommands\_SwiftInsertDatum** | 593; valid for parts; **DimXpert toolbar > Datum** |
| **swCommands\_SwiftInsertDatumTarget** | 3450; Inserts a DimXpert datum target; **Tools menu > MBD Dimension > Datum Target** |
| **swCommands\_SwiftInsertDimension** | 592; valid for parts; **DimXpert toolbar > Location Dimension** |
| **swCommands\_SwiftInsertGeneralProfileTolerance** | 3325; adds a Profile of Surface geometric tolerance to an open part; **DimXpert toolbar > General Profile Tolerance** |
| **swCommands\_SwiftInsertGtol** | 594; valid for parts, opens the GeometricTolerance Properties dialog; **DimXpert toolbar > Geometric Tolerance** |
| **swCommands\_SwiftInsertPatternFeature** | 627; valid for parts, opens the DimXpert Pattern/Collection PropertyManager page; **DimXpert toolbar > Pattern Feature** |
| **swCommands\_SwiftInsertSizeDimension** | 625; valid for parts; **DimXpert toolbar > Size Dimension** |
| **swCommands\_SwiftRecognizeFeatures** | 591; valid for parts; **DimXpert toolbar > Auto Dimension Scheme** |
| **swCommands\_SwiftShowConstraintStatus** | 595; valid for parts; **DimXpert toolbar > Show Tolerance Status** |
| **swCommands\_SWPremium** | 3432; SOLIDWORKS Premium |
| **swCommands\_SWUltimate** | 3532; SOLIDWORKS Ultimate |
| **swCommands\_TabAndSlot** | 3234; adds a tab and slot feature; **Sheet Metal toolbar > Tab and Slot** |
| **swCommands\_Table\_Cell\_Sub\_Total** | 1975; inserts "Sub-total" into a selected table cell |
| **swCommands\_Table\_Cell\_Total** | 1976; inserts "Total" into a selected table cell |
| **swCommands\_TableDrivenPattern** | 300; valid for parts with a selected sketch; **Features toolbar > Table Driven Pattern** |
| **swCommands\_TangentArc** | 69; **Layout Tools** or **Sketch toolbar > Tangent Arc** |
| **swCommands\_TangentSnap** | 528; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; **Quick Snaps toolbar > Tangent Snap** |
| **swCommands\_Text** | 109; **Sketch toolbar > Text** |
| **swCommands\_Thicken** | 97; valid for a part with two or more knit surfaces, opens the Thicken PropertyManager page; **Features toolbar > Thicken** |
| **swCommands\_ThickenedCut** | 98; valid for a part with two or more knit surfaces, opens the Cut-Thicken PropertyManager page; **Features toolbar > Thickened Cut** |
| **swCommands\_TileHorizontally** | 581; **Standard toolbar > Tile Horizontally** |
| **swCommands\_TileVertically** | 582; **Standard toolbar > Tile Vertically** |
| **swCommands\_TitleBlockDefine** | 2852; valid for a drawing with its sheet format open, opens the Title Block Table PropertyManager page; **Sheet Format toolbar > Title Block Fields** |
| **swCommands\_TitleBlockEdit** | 2853; valid for a drawing sheet format with a title block defined, opens the Title Block Table; in the FeatureManager design tree, *sheet\_folder* **>** *sheet\_format\_folder* **>** *title\_block\_table* **RMB menu > Title Block Fields** |
| **swCommands\_TitleBlockEnterData** | 2854; valid for a drawing sheet format with a title block defined, opens the Title Block Data PropertyManager page; in the FeatureManager design tree, *sheet\_folder* **>** *sheet\_format\_folder* **>** *title\_block\_table* **RMB menu > Enter Title Block Data** |
| **swCommands\_TitleBlockTable** | 2949; valid for parts and assemblies, opens the Title Block Table PropertyManager page; **Table toolbar > Title Block Table** |
| **swCommands\_Toggle\_Context\_Switch** | 1990; **CommandManager RMB menu > Use Large Buttons With Text** |
| **swCommands\_Toggle\_Grid** | 1509; valid when inserting a Grid System; in the graphics area, **RMB menu > Display Grid** |
| **swCommands\_Toggle\_MagMate** | 3216; valid for assemblies only, toggles magnetic mates; **alt-M** or **Tools menu or toolbar > Magnetic Mate ON/OFF** |
| **swCommands\_Toggle\_Magnified\_Selection** | 3135; **Standard toolbar > Magnified Selection** |
| **swCommands\_Toggle\_Notes\_UpperCase** | 3105; toggles Note case to upper case; press F3 |
| **swCommands\_Toggle\_Ole\_Owner** | 1555; valid for a drawing with a selected object; in the graphics area, *ole\_object* **RMB menu > Show on this sheet only** |
| **swCommands\_Toggle\_Pic\_Texture** | 1900; valid for a selected picture with a texture; in the graphics area, *pic\_with\_texture* **RMB menu > Hide/Show Texture** |
| **swCommands\_Toggle\_Power\_Dim\_Mode** | 2445; valid when Power Assist PropertyManager page is open; in the graphics area, **RMB menu > DimXpert dimension toggle** |
| **swCommands\_Toggle\_Smart\_Dim\_Mode** | 2444; valid when Power Assist PropertyManager page is open; in the graphics area, **RMB menu > Smart dimension toggle** |
| **swCommands\_Toggle\_Viewing\_Dir** | 1593; valid for a selected drawing view arrow; in the graphics area, *sel\_view\_arrow* **RMB menu > Toggle View Direction** |
| **swCommands\_ToggleGraphicsDisplay** | 3246; **Tools toolbar > Display Graphics Components** |
| **swCommands\_ToggleInstant2D** | 3188; **Sketch toolbar > Instant2D** |
| **swCommands\_ToggleSelectionFilters** | 273; **Selection Filters toolbar > Toggle Selection Filters** |
| **swCommands\_ToggleSelectionFilterToolbar** | 356; **Standard toolbar > Toggle Selection Filter Toolbar** |
| **swCommands\_TolXpert** | 612; alternative to swCommands\_Toolbar\_DimXpert; **View menu > Toolbars > DimXpert** |
| **swCommands\_Toogle\_Bwrtree** | 2446; valid in Full Screen mode; **Full Screen toolbar > Hide/Show FeatureManager** |
| **swCommands\_Toolbar\_2dto3d** | 1182; alternative to swCommands\_2dto3d\_Toolbar; **View menu > Toolbars > 2D to 3D** |
| **swCommands\_Toolbar\_Adv\_Struct\_System** | 3334; **View menu > Toolbars > Structure System** |
| **swCommands\_Toolbar\_Align** | 1180; alternative to swCommands\_Align; **View menu > Toolbars > Align** |
| **swCommands\_Toolbar\_Annotation** | 1167; alternative to swCommands\_Annotations; **View menu > Toolbars > Annotation** |
| **swCommands\_Toolbar\_Assembly** | 1155; alternative to swCommands\_Assemblies; **View menu > Toolbars > Assembly** |
| **swCommands\_Toolbar\_Context** | 1205; **View menu > Toolbars > CommandManager** |
| **swCommands\_Toolbar\_Curve** | 1175; alternative to swCommands\_Curves; **View menu > Toolbars > Curves** |
| **swCommands\_Toolbar\_DimXpert** | 1192; alternative to swCommands\_TolXpert; **View menu > Toolbars > DimXpert** |
| **swCommands\_Toolbar\_Display\_States** | 2809; **View menu > Toolbars > Display States** |
| **swCommands\_Toolbar\_Drawing** | 1156; alternative to swCommands\_Drawings; **View menu > Toolbars > Drawing** |
| **swCommands\_Toolbar\_Exploderoute** | 1183; alternative to swCommands\_ExplodeSketch; **View menu > Toolbars >** **Explode Sketch** |
| **swCommands\_Toolbar\_Features** | 1157; alternative to swCommands\_Features; **View menu > Toolbars > Features** |
| **swCommands\_Toolbar\_Font** | 1166; alternative to swCommands\_Fonts; **View menu > Toolbars > Formatting** |
| **swCommands\_Toolbar\_Handsketch** | 3242; valid only for a sketch opened in SOLIDWORKS running on supporting pen/stylus hardware; alternative to swCommands\_Handsketch\_Toolbar |
| **swCommands\_Toolbar\_Inference** | 1190; alternative to swCommands\_ClickHereToSeeThePreview; **View menu > Toolbars > Quick Snaps** |
| **swCommands\_Toolbar\_Inkmarkup** | 3437; **View menu > Toolbars > Markup** |
| **swCommands\_Toolbar\_Layer** | 1180; alternative to swCommands\_Layer\_Toolbar; **View menu > Toolbars > Layer** |
| **swCommands\_Toolbar\_Layout\_Tools** | 2816; alternative to swCommands\_Layout; **View menu > Toolbars > Layout Tools** |
| **swCommands\_Toolbar\_Lifecycle\_And\_Collaboration** | 3484; For SOLIDWORKS Connected only; Activates the Lifecycle and Collaboration toolbar; **View menu > Toolbars > Lifecycle and Collaboration** |
| **swCommands\_Toolbar\_Lineformat** | 1165; alternative to swCommands\_LineFormats; **View menu > Toolbars > Line Format** |
| **swCommands\_Toolbar\_Macro** | 1159; alternative to swCommands\_Macros; **View menu > Toolbars > Macro** |
| **swCommands\_Toolbar\_Mold** | 1172; alternative to swComnmands\_Molds; **View menu > Toolbars > Mold Tools** |
| **swCommands\_Toolbar\_Office** | 1187; alternative to swCommands\_SolidworksOffice; **View menu > Toolbars > SOLIDWORKS Add-ins** |
| **swCommands\_Toolbar\_OneClick** | 3289; **Tools menu > 3DEXPERIENCE Simulation Connector** |
| **swCommands\_Toolbar\_Refgeom** | 1178; alternative to swCommands\_ReferenceGeometry; **View menu > Toolbars > Reference Geometry** |
| **swCommands\_Toolbar\_Render** | 2963; alternative to swCommands\_RenderToolbar; **View menu > Toolbars > Render Tools** |
| **swCommands\_Toolbar\_ScreenCapture** | 2812; alternative to swCommands\_ScreenCaptureToolbar; **View menu > Toolbars > Screen Capture** |
| **swCommands\_Toolbar\_Sel\_Filter** | 1160; alternative to swCommands\_Filter\_Toolbar; **View menu > Toolbars > Selection Filter** |
| **swCommands\_Toolbar\_Sht\_Mtl** | 1173; alternative to swCommands\_SheetMetal; **View menu > Toolbars > Sheet Metal** |
| **swCommands\_Toolbar\_Sketch** | 1161; alternative to swCommands\_SketchToolbar; **View menu > Toolbars > Sketch** |
| **swCommands\_Toolbar\_Sketch\_Group** | 2028; alternative to swCommands\_Blocks; **View menu > Toolbars > Blocks** |
| **swCommands\_Toolbar\_Sketch\_Rels** | 1162; alternative to swCommands\_DimensionRelations; **View menu > Toolbars > Dimensions/Relations** |
| **swCommands\_Toolbar\_Spline\_Tools** | 1185; alternative to swCommands\_Splines; **View menu > Toolbars > Spline Tools** |
| **swCommands\_Toolbar\_Standard** | 1153; alternative to swCommands\_Standard; **View menu > Toolbars > Standard** |
| **swCommands\_Toolbar\_Stdview** | 1169; alternative to swCommands\_StandardViews; **View menu > Toolbars > Standard Views** |
| **swCommands\_Toolbar\_Surface** | 1174; alternative to swCommands\_Surfaces; **View menu > Toolbars > Surfaces** |
| **swCommands\_Toolbar\_Table** | 1191; alternative to swCommands\_EnterTheOffsetOfTheSupportArea; **View menu > Toolbars > Table** |
| **swCommands\_Toolbar\_Tools** | 1179; alternative to swCommands\_Tools; **View menu > Toolbars > Tools** |
| **swCommands\_Toolbar\_View** | 1154; alternative to swCommands\_View; **View menu > Toolbars > View** |
| **swCommands\_Toolbar\_Web** | 1164; alternative to swCommands\_Web; **View menu > Toolbars > Web** |
| **swCommands\_Toolbar\_Weldment** | 1189; alternative to swCommands\_Weldments; **View menu > Toolbars > Weldments** |
| **swCommands\_ToolingSplit** | 464; valid for parts containing 3 surface bodies (core, cavity, and parting) and a selected face or plane perpendicular to the direction of pull; **Mold Tools toolbar > Tooling Split** |
| **swCommands\_Tools** | 496 alternative to swCommands\_Toolbar\_Tools; **View menu > Toolbars > Tools** |
| **swCommands\_Tools\_Addins** | 1073; opens the Add-Ins dialog; **Tools menu > Add-Ins** |
| **swCommands\_Tools\_Addview\_Ff** | 1245; valid for drawings with the Relative View PropertyManager page open, opens the Open dialog; in the graphics area, **RMB menu > Insert From File** |
| **swCommands\_Tools\_Align\_Horz** | 889; valid for a selected drawing view; **Tools > Align Drawing View > Horizontal Edge** |
| **swCommands\_Tools\_Align\_Vert** | 890; valid for a selected drawing view; **Tools > Align Drawing View > Vertical Edge** |
| **swCommands\_Tools\_Arrange\_Components** | 1254; valid for assemblies, opens the Assembly Structure Editing dialog; **Tools menu > Reorganize Components** |
| **swCommands\_Tools\_Configuration** | 973; valid for parts and assemblies, opens the SOLIDWORKS ConfigurationManager dialog |
| **swCommands\_Tools\_Crop\_Delete** | 1389; valid for a selected Crop View in a drawing; *crop\_view* **RMB menu > Crop View > Remove Crop** |
| **swCommands\_Tools\_Crop\_Edit** | 1388; valid for a selected Crop View in a drawing; *crop\_view* **RMB menu > Crop View > Edit Crop** |
| **swCommands\_Tools\_Customize** | 1137; opens the Customize dialog; **Tools menu > Customize** |
| **swCommands\_Tools\_Dim\_Pref** | 945; valid for an open model, opens the Document Properties dialog; in the FeatureManager design tree, *top\_level\_document* **RMB menu > Document Properties** |
| **swCommands\_Tools\_Drw\_Autoregen** | 1573; valid for a selected drawing; in the FeatureManager design tree, *drawing* **RMB menu > Automatic view update** |
| **swCommands\_Tools\_Drw\_Dimtext\_Link** | 636; valid for a selected drawing; in the FeatureManager design tree, *drawing* **RMB menu > Link external dim text** |
| **swCommands\_Tools\_Font\_Tan** | 1078; valid for parts; **View menu > Display > Tangent Edges as Phantom** |
| **swCommands\_Tools\_Font\_Tangent\_Edges** | 1546; valid for drawings for a selected view; **View menu > Display > Tangent Edges With Font** |
| **swCommands\_Tools\_Hide\_Dv** | 979; valid for drawings; **View menu > Hide / Show > Hidden Views** |
| **swCommands\_Tools\_Macro\_Mru\_1** | 2376; opens the first macro in the recent macros list in Microsoft Visual Basic for Applications; **Tools menu > Macro >** *first\_macro* |
| **swCommands\_Tools\_Macro\_Mru\_2** | 2377; opens the second macro in the recent macros list in Microsoft Visual Basic for Applications; **Tools menu > Macro >** *second\_macro* |
| **swCommands\_Tools\_Macro\_Mru\_3** | 2378; opens the third macro in the recent macros list in Microsoft Visual Basic for Applications; **Tools menu > Macro >** *third\_macro* |
| **swCommands\_Tools\_Macro\_Mru\_4** | 2379; opens the fourth macro in the recent macros list in Microsoft Visual Basic for Applications; **Tools menu > Macro >** *fourth\_macro* |
| **swCommands\_Tools\_Macro\_Mru\_5** | 2380; opens the fifth macro in the recent macros list in Microsoft Visual Basic for Applications; **Tools menu > Macro >** *fifth\_macro* |
| **swCommands\_Tools\_Macro\_Mru\_6** | 2381; opens the sixth macro in the recent macros list in Microsoft Visual Basic for Applications; **Tools menu > Macro >** *sixth\_macro* |
| **swCommands\_Tools\_Macro\_Mru\_7** | 2382; opens the seventh macro in the recent macros list in Microsoft Visual Basic for Applications; **Tools menu > Macro >** *seventh\_macro* |
| **swCommands\_Tools\_Macro\_Mru\_8** | 2383; opens the eighth macro in the recent macros list in Microsoft Visual Basic for Applications; **Tools menu > Macro >** *eighth\_macro* |
| **swCommands\_Tools\_Macro\_Mru\_9** | 2384; opens the ninth macro in the recent macros list in Microsoft Visual Basic for Applications; **Tools menu > Macro >** *ninth\_macro* |
| **swCommands\_Tools\_Remove\_Tan** | 1079; valid for parts; **View menu > Display > Tangent Edges Removed** |
| **swCommands\_Tools\_Remove\_Tangent\_Edges** | 1515; valid for drawings for a selected view; **View menu > Display > Tangent Edges Removed** |
| **swCommands\_Tools\_Show\_Tan** | 1077; valid for parts; **View menu > Display > Tangent Edges Visible** |
| **swCommands\_Tools\_Show\_Tangent\_Edges** | 1545; valid for drawings for a selected view; **View menu > Display > Tangent Edges Visible** |
| **swCommands\_ToolsGrid** | 2791; opens the Document Properties - Grid/Snap dialog; **Sketch toolbar > Grid/Snap** |
| **swCommands\_ToolsSensor** | 2892; opens the Sensor PropertyManager page; **Tools toolbar > Sensor** |
| **swCommands\_Top** | 163; **View toolbar > View Orientation > Top** |
| **swCommands\_Top\_Left** | 923; valid for a selected Excel-based BOM in a drawing view; *Excel\_BOM* **RMB menu > Anchor > Top Left** |
| **swCommands\_Top\_Right** | 920; valid for a selected Excel-based BOM in a drawing view; *Excel\_BOM* **RMB menu > Anchor > Top Right** |
| **swCommands\_Translate\_Drawing** | 638; valid for a drawing, opens the Move Drawing dialog; in the FeatureManager design tree, *drawing* **RMB menu > Move** |
| **swCommands\_Triad\_Blob\_Align\_To** | 2449; valid after *component* **RMB menu > Move with Triad** command in assembly; in the graphics area, *triad\_center\_ball* **RMB menu > Align to** |
| **swCommands\_TrimAsGroupWithPreAdvStructMember** | 3362; trims with previous advanced structure member |
| **swCommands\_TrimAsIndAdvStructMember** | 3363; trims as an individual advanced structural member |
| **swCommands\_TrimCornerCorner** | 2792; valid for a flattened sheet metal part with a selected corner, opens the Corner-Trim PropertyManager page; **Sheel Metal toolbar > Corner-Trim** |
| **swCommands\_TrimEntities** | 59; valid for an open sketch, opens the Trim PropertyManager page; **Sketch** or **Layout Tools toolbar > Trim Entities** |
| **swCommands\_Trimetric** | 467; **Standard Views toolbar > Trimetric** |
| **swCommands\_TrimExtend** | 466; valid for weldments, opens the Trim/Extend PropertyManager page; **Weldment toolbar > Trim/Extend** |
| **swCommands\_TrimSurface** | 302; valid for a part with one or more selected surfaces, opens the Trim Surface PropertyManager page; **Surfaces toolbar > Trim Surface** |
| **swCommands\_Tube\_Properties** | 3012; valid for the SOLIDWORKS Routing add-in and a selected tube in an open flexible tube route; *flex\_tube* **RMB menu > Tube Properties** |
| **swCommands\_Turn** | 606; valid for a model with a camera; **View menu > Modify > Turn Camera** |
| **swCommands\_TwoViewHorizontal** | 550; **View toolbar > View Orientation > Two View - Horizontal** |
| **swCommands\_TwoViewVertical** | 551; **View toolbar > View Orientation > Two View - Vertical** |
| **swCommands\_Unblank\_Atom\_Body** | 1028; in the FeatureManager design tree, click *body\_folder* **RMB context toolbar > Show** |
| **swCommands\_Unblank\_Atom\_Body2** | 2731; valid for a part with a solid or surface body; in the FeatureManager design tree, *body\_folder* **>** *body* **RMB context toolbar > Show** |
| **swCommands\_Unblank\_Grid\_Comp** | 3001; valid for a part or assembly with the GridSystem PropertyManager page open and the grid feature component hidden; in the graphics area, **RMB menu > Show** |
| **swCommands\_Unblank\_Origin\_Sketch** | 2469; valid for a hidden profile sketch; in the graphics area, *prof\_sketch* **RMB menu > Show** |
| **swCommands\_Unblank\_Part\_Body** | 1413; valid for a selected face of an atom feature in an assembly; in the graphics area, *sel\_face* **RMB menu > Show Solid Body** |
| **swCommands\_Unblank\_Pic\_Feat** | 2486; valid for a selected hidden picture feature object; in the graphics area, *pic\_feat* **RMB menu > Show** |
| **swCommands\_Unblank\_Refgeom** | 896; valid for a selected reference geometry; in the FeatureManager design tree, *ref\_geom* **RMB menu > Show** |
| **swCommands\_Unblank\_Sketch** | 955; valid for a selected drawing sketch; in the graphics area, *sketch* **RMB menu > Show** |
| **swCommands\_Unbreak\_View** | 1520; valid for a drawing break view; in the FeatureManager design tree, *break\_view* **RMB menu > Un-Break View** |
| **swCommands\_Underive\_Sketch** | 1010; valid for a selected derived sketch; in the FeatureManager design tree, *sketch\_derived* **RMB menu > Underive** |
| **swCommands\_Underline** | 149; valid for selected text; **Formatting toolbar > Underline** |
| **swCommands\_Undo** | 586; **Standard toolbar > Undo** |
| **swCommands\_Undo\_Eq** | 633; dialog resource **Undo** |
| **swCommands\_Unfix\_Component** | 959; valid for a selected fixed assembly component; in the FeatureManager design tree, *comp* **RMB menu > Float** |
| **swCommands\_Unfold** | 326; valid for sheet metal parts; **Sheet Metal toolbar > Unfold** |
| **swCommands\_Unfreeze\_All** | 3014; valid for models where feature freeze is enabled, and the selected feature is frozen; in the FeatureManager design tree, *feature* **RMB menu > Unfreeze All Features** |
| **swCommands\_Ungroup** | 327; valid for multi-selected annotations or dimensions; **Align toolbar > Ungroup** |
| **swCommands\_Unlink\_Dim** | 1544; valid for sketches with dimensions with shared parameters, opens the Shared Values dialog; in the graphics area, *shared\_dimension* **RMB menu** **> Unlink Value** |
| **swCommands\_Unload\_Hidden\_Comps** | 2868; valid for a selected assembly; in the FeatureManager design tree, *top\_level\_assy* **RMB menu > Unload Hidden Components** |
| **swCommands\_Unlock\_Bom** | 914; valid for a drawing view with an Excel-based Bill of Materials; in the graphics area, *BOM\_table* **RMB menu > Anchor > Unlock from Anchor** |
| **swCommands\_Unlock\_Configuration** | 1846; valid in a PDM-enabled environment with a locked configuration; in ConfigurationManager, *locked\_config* **RMB menu > Unlock Configuration** |
| **swCommands\_Unslant\_Dim** | 1533; valid for a selected dimension with a witness line that is slanted; in the graphics area, *dim\_with\_slanted\_witness* **RMB menu > Display Options > Remove Slant** |
| **swCommands\_Unsuppress** | 15; valid for one or more selected suppressed features; **Edit menu > Unsuppress > This Configuration** |
| **swCommands\_UnsuppressWithDependents** | 50; valid for one or more selected suppressed features; **Edit menu > Unsuppress with Dependents > This Configuration** |
| **swCommands\_UntrimSurface** | 400; valid for a part with a selected face or edge to patch, opens the Untrim Surface PropertyManager page; **Surfaces toolbar > Untrim Surface** |
| **swCommands\_Update\_Cutlist** | 2602; valid for a part with a selected Cut list folder; in the FeatureManager design tree, *cut\_list\_folder* **RMB menu > Update** |
| **swCommands\_Update\_Msg** | 2786; dialog resource **Update** |
| **swCommands\_Update\_Std\_View** | 885; **View toolbar > View Orientation > More options > Orientation dialog > Update Standard Views** |
| **swCommands\_UpdateAllSpeedpakConfig** | 3070; valid for assemblies; **Assembly toolbar > Update Speedpak** |
| **swCommands\_UpdateImportedModel** | 3343; updates an imported model |
| **swCommands\_UpdateView** | 385; valid for drawings with a selected view; **Drawing toolbar > Update View** |
| **swCommands\_User\_Communities** | 3463; **Help menu > User Communities** |
| **swCommands\_User\_Defined\_Route** | 3189; valid for the SOLIDWORKS Routing or the SOLDWORKS Electrical add-in, opens the Projects Manager dialog; **Routing** or **SOLIDWORKS Electrical: Application toolbar > User Defined Route** |
| **swCommands\_User\_Job\_Cancel** | 699; dialog resource **Cancel** |
| **swCommands\_User\_Toolbar\_Max** | 1628; maximum allowed number of toolbar commands |
| **swCommands\_User\_Toolbar\_Min** | 1627; minimum allowed number of toolbar commands |
| **swCommands\_Userdefined\_Add\_Fitting** | 3165; valid for SOLIDWORKS Routing add-in with an open route; **User Defined toolbar > Add Fitting** |
| **swCommands\_Userdefined\_Rt\_On\_Fly** | 3166; valid for SOLIDWORKS Routing add-in with an open route; **User Defined toolbar > Start at Point** |
| **swCommands\_Userdefined\_Rt\_Properties** | 3168; valid for SOLIDWORKS Routing add-in with an open route; **User Defined toolbar > Route Properties** |
| **swCommands\_UserMacro01** | 174; runs the first macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro02** | 175; runs the second macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro03** | 176; runs the third macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro04** | 177; runs the fourth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro05** | 178; runs the fifth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro06** | 179; runs the sixth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro07** | 180; runs the seventh macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro08** | 181; runs the eighth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro09** | 182; runs the ninth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro10** | 183; runs the tenth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro11** | 184; runs the eleventh macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro12** | 185; runs the twelfth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro13** | 186; runs the thirteenth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro14** | 187; runs the fourteenth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro15** | 188; runs the fifteenth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro16** | 189; runs the sixteenth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro17** | 190; runs the seventeenth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro18** | 191; runs the eighteenth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro19** | 192; runs the nineteenth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro20** | 193; runs the twentieth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro21** | 194; runs the twenty-first macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro22** | 195; runs the twenty-second macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro23** | 196; runs the twenty-third macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro24** | 197; runs the twenty-fourth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro25** | 198; runs the twenty-fifth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro26** | 199; runs the twenty-sixth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro27** | 200; runs the twenty-seventh macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro28** | 201; runs the twenty-eighth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro29** | 202; runs the twenty-ninth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro30** | 203; runs the thirtieth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro31** | 204; runs the thirty-first macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro32** | 205; runs the thirty-second macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro33** | 206; runs the thirty-third macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro34** | 207; runs the thirty-fourth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro35** | 208; runs the thirty-fifth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro36** | 209; runs the thirty-sixth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro37** | 210; runs the thirty-seventh macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro38** | 211; runs the thirty-eighth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro39** | 212; runs the thirty-ninth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro40** | 213; runs the fortieth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro41** | 214; runs the forty-first macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro42** | 215; runs the forty-second macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro43** | 216; runs the forty-third macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro44** | 217; runs the forty-fourth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro45** | 218; runs the forty-fifth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro46** | 219; runs the forty-sixth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro47** | 220; runs the forty-seventh macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro48** | 221; runs the forty-eighth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro49** | 222; runs the forty-ninth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro50** | 223; runs the fiftieth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro51** | 224; runs the fifty-first macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro52** | 225; runs the fifty-second macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro53** | 226; runs the fifty-third macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro54** | 227; runs the fifty-fourth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro55** | 228; runs the fifty-fifth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro56** | 229; runs the fifty-sixth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro57** | 230; runs the fifty-seventh macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro58** | 231; runs the fifty-eighth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro59** | 232; runs the fifty-ninth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro60** | 233; runs the sixtieth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro61** | 234; runs the sixty-first macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro62** | 235; runs the sixty-second macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro63** | 236; runs the sixty-third macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro64** | 237; runs the sixty-fourth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro65** | 238; runs the sixty-fifth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro66** | 239; runs the sixty-sixth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro67** | 240; runs the sixty-seventh macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro68** | 241; runs the sixty-eighth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro69** | 242; runs the sixty-ninth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro70** | 243; runs the seventieth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro71** | 244; runs the seventy-first macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro72** | 245; runs the seventy-second macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro73** | 246; runs the seventy-third macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro74** | 247; runs the seventy-fourth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro75** | 248; runs the seventy-fifth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro76** | 249; runs the seventy-sixth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro77** | 250; runs the seventy-seventh macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro78** | 251; runs the seventy-eighth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro79** | 252; runs the seventy-ninth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro80** | 253; runs the eightieth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro81** | 254; runs the eighty-first macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro82** | 255; runs the eighty-second macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro83** | 256; runs the eighty-third macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro84** | 257; runs the eighty-fourth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro85** | 258; runs the eighty-fifth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro86** | 259; runs the eighty-sixth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro87** | 260; runs the eighty-seventh macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro88** | 261; runs the eighty-eighth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro89** | 262; runs the eighty-ninth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro90** | 263; runs the nintieth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro91** | 264; runs the ninety-first macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro92** | 265; runs the ninety-second macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro93** | 266; runs the ninety-third macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro94** | 267; runs the ninety-fourth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro95** | 268; runs the ninety-fifth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro96** | 269; runs the ninety-sixth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro97** | 270; runs the ninety-seventh macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_UserMacro98** | 271; runs the ninety-eighth macro defined by **Macro toolbar > New Macro Button** |
| **swCommands\_VerticalBreak** | 110; valid for a drawing and a selected view; **Drawing toolbar > Break** |
| **swCommands\_VerticalDimension** | 68; **Dimensions/Relations toolbar > Vertical Dimension** |
| **swCommands\_VerticalOrdinateDimension** | 348; **Dimensions/Relations toolbar > Vertical Ordinate Dimension** |
| **swCommands\_View** | 498; alternative to swCommands\_Toolbar\_View; **View menu > Toolbars > View** |
| **swCommands\_View\_Animate\_Collapse\_Assembly** | 1983; valid for an assembly with a selected exploded view, opens the Animation Controller dialog; in the ConfigurationManager, *ExplView* **RMB menu > Animate collapse** |
| **swCommands\_View\_Animate\_Explode\_Assembly** | 1982; valid for an assembly with a selected exploded view that was collapsed, opens the Animation Controller dialog; in the ConfigurationManager, *ExplView* **RMB menu > Animate explode** |
| **swCommands\_View\_Assy\_Full** | 748; valid for an assembly with a component being edited in context; in the graphics area, **RMB menu > Assembly Transparency > Force Transparency** |
| **swCommands\_View\_Assy\_Maintain** | 749; valid for an assembly with a component being edited in context; in the graphics area, **RMB menu > Assembly Transparency > Maintain Transparency** |
| **swCommands\_View\_Assy\_Opaque** | 747; valid for an assembly with a component being edited in context; in the graphics area, **RMB menu > Assembly Transparency > Opaque** |
| **swCommands\_View\_Clear\_Select** | 1541; valid in many contexts; pop-up menu item "Clear Selections" |
| **swCommands\_View\_Collapse\_Assembly** | 995; valid for an assembly with a selected explode view; in the ConfigurationManager, *exploded\_view* **RMB menu > Collapse** |
| **swCommands\_View\_Disp\_Hideall** | 1810; **View menu > Hide / Show > Hide All Types** |
| **swCommands\_View\_Edit\_Perspective** | 1043; valid for a perspective view, opens the Perspective View PropertyManager page; **View menu > Modify > Perspective** |
| **swCommands\_View\_Explode\_Assembly** | 993; valid for an assembly with a selected explode view that is collapsed; in the ConfigurationManager, *exploded\_view* **RMB menu > Explode** |
| **swCommands\_View\_Fm\_By\_Dep** | 1031; **View menu > User Interface > FeatureManager Tree > By Dependencies** |
| **swCommands\_View\_Fm\_By\_Feat** | 1030; **View menu > User Interface > FeatureManager Tree > By Features** |
| **swCommands\_View\_Hide\_Behind\_Plane** | 875; valid for a drawing document, opens the Hide Behind Plane dialog; in the FeatureManager design tree, *ref\_plane* **RMB menu > Hide Behind Plane** |
| **swCommands\_View\_Hideshow** | 1390; valid for part or assembly with bodies, opens the Hide / Show Bodies PropertyManager page; **View menu > Hide / Show > Bodies** |
| **swCommands\_View\_Lock\_Camera** | 1061; valid for a model with a selected camera in DisplayManager; in DisplayManager, **Camera >** *Camera1* **> RMB menu > Lock Camera** |
| **swCommands\_View\_Move\_Manipulator** | 1993; valid for assemblies; in the graphics area, *comp* **RMB menu > Move with Triad** |
| **swCommands\_View\_Normal\_To** | 1640; valid for annotation, BOM, and title block tables; in the graphics area, *table* **RMB menu > Normal To** |
| **swCommands\_View\_Orientation\_Rmb** | 916; valid in many contexts; in the graphics area, **RMB menu > View Orientation** |
| **swCommands\_View\_Orientation\_ViewBox** | 3081; **View toolbar > View Orientation > View Selector** |
| **swCommands\_View\_Query\_Select** | 891; valid in many contexts; in the graphics area, **RMB menu > Select Other** |
| **swCommands\_View\_Rotate\_About\_Vertical** | 3071; **View menu > Modify > Rotate About Scene Floor** |
| **swCommands\_View\_Rotateminusx** | 1472; Press DOWN ARROW |
| **swCommands\_View\_Rotateminusy** | 1469; Press LEFT ARROW |
| **swCommands\_View\_Rotateminusz** | 1471; Press Alt-LEFT ARROW |
| **swCommands\_View\_Rotateplusx** | 1473; Press UP ARROW |
| **swCommands\_View\_Rotateplusy** | 1468; Press RIGHT ARROW |
| **swCommands\_View\_Rotateplusz** | 1470; Press Alt-RIGHT ARROW |
| **swCommands\_View\_Rotx\_Minusninety** | 1474; Press Shift-DOWN ARROW |
| **swCommands\_View\_Rotx\_Plusninety** | 1475; Press Shift-UP ARROW |
| **swCommands\_View\_Roty\_Minusninety** | 1476; Press Shift-LEFT ARROW |
| **swCommands\_View\_Roty\_Plusninety** | 1477; Press Shift-RIGHT ARROW |
| **swCommands\_View\_Ruler** | 1303; valid for drawings; **View menu > User Interface > Rulers** |
| **swCommands\_View\_Sheet\_Next** | 898; valid for drawings; **View menu > Next Sheet** |
| **swCommands\_View\_Sheet\_Previous** | 897; valid for drawings; **View menu > Previous Sheet** |
| **swCommands\_View\_ShowAnnotationTextExpression** | 3538; **View menu > Hide / Show > Annotation Text Expression** |
| **swCommands\_View\_Showantn\_Linkerrors** | 1895; **View menu > Hide / Show > Annotation Link Errors** |
| **swCommands\_View\_Showantn\_Linkvar** | 2145; **View menu > Hide / Show > Annotation Link Variables** |
| **swCommands\_View\_Showhide\_Tb** | 2756; **View menu > User Interface > Toolbars** |
| **swCommands\_View\_This\_Camera** | 1060; valid for a selected camera; in the DisplayManager, *camera* **RMB menu > Camera View** |
| **swCommands\_View\_Transminusx** | 1479; Press Ctrl-LEFT ARROW |
| **swCommands\_View\_Transminusy** | 1481; Press Ctrl-UP ARROW |
| **swCommands\_View\_Transplusx** | 1478; Press Ctrl-RIGHT ARROW |
| **swCommands\_View\_Transplusy** | 1480; Press Ctrl-DOWN ARROW |
| **swCommands\_View\_Undo\_Last** | 1584; valid for parts; **View menu > Modify > Previous View** |
| **swCommands\_View\_Zoom\_About\_Center** | 1803; **View menu > Modify > Zoom About Screen Center** |
| **swCommands\_View\_Zoomin** | 1482; Press Shift-Z |
| **swCommands\_View\_Zoomout** | 1483; Press Z |
| **swCommands\_View3DSketchDimensions** | 562; **View toolbar > View Sketch Dimensions** |
| **swCommands\_View3DSketchPlane** | 561; **View toolbar > View 3D Sketch Plane** |
| **swCommands\_ViewAllAnnotations** | 404; **View toolbar > View All Annotations** |
| **swCommands\_ViewAssemAnnotations** | 3120; **View toolbar > View Top Level Annotations** |
| **swCommands\_ViewAssemEnvelopes** | 3423; **View toolbar > View Top Level Envelopes** |
| **swCommands\_ViewAxes** | 339; **View toolbar > View Axes** |
| **swCommands\_ViewBendLines** | 3468; Controls the visibility of bend lines; **View menu > Hide / Show > Bend Lines** or **View toolbar > View Bend Lines** |
| **swCommands\_ViewCameras** | 608; **View toolbar > View Cameras** |
| **swCommands\_ViewCompAnnotations** | 3119; **View toolbar > View Component Annotations** |
| **swCommands\_ViewCompEnvelopes** | 3422; **View toolbar > View Component Envelopes** |
| **swCommands\_ViewCoordinateSystems** | 153; **View toolbar > View Coordinate Systems** |
| **swCommands\_ViewCosmeticWeldSymbol** | 3004; **View toolbar > View Weld Beads** |
| **swCommands\_ViewCurves** | 402; **View toolbar > View Curves** |
| **swCommands\_ViewDatumReferenceFrame** | 3184; **View toolbar > View Datum Reference Frame** |
| **swCommands\_ViewDecals** | 2925; **View toolbar > View Decals** |
| **swCommands\_ViewDimNames** | 2954; **View toolbar > View Dimension Names** |
| **swCommands\_ViewGlobalBBox** | 3323; controls the visibility of the bounding box; **View menu > View Bounding Box** |
| **swCommands\_ViewLights** | 607; **View toolbar > View Lights** |
| **swCommands\_ViewLiveSections** | 2875; **View toolbar > View Live Section Planes** |
| **swCommands\_ViewOrientation** | 341; Press SPACEBAR |
| **swCommands\_ViewOrigins** | 126; **View toolbar > View Origins** |
| **swCommands\_ViewPartingLines** | 547; **View toolbar > View Parting Lines** |
| **swCommands\_ViewPlanes** | 338; **View toolbar > View Planes** |
| **swCommands\_ViewPoints** | 511; **View toolbar > View Points** |
| **swCommands\_Viewport\_Unsplit\_Camera** | 2185; valid when the Camera1 PropertyManager page is open; in the Camera1 PropertyManager page, click **X**. |
| **swCommands\_ViewRoutingPoints** | 510; **View toolbar > View Routing Points** |
| **swCommands\_ViewSimResults** | 3201; opens the View Simulation Results PropertyManager page; valid only if the SOLIDWORKS Simulation add-in is loaded, and Simulation study results are available for the current model; **View toolbar > View Simulation Results** |
| **swCommands\_ViewSimulationSymbol** | 2992; **View toolbar > View Simulation Symbols** |
| **swCommands\_ViewSketches** | 403; **View toolbar > View Sketches** |
| **swCommands\_ViewSketchRelations** | 440; **View toolbar > View Sketch Relations** |
| **swCommands\_ViewTemporaryAxes** | 99; **View toolbar > View Temporary Axes** |
| **swCommands\_Visual\_State\_Clear\_Override** | 785; valid for assemblies with display settings; in the Display Pane, **RMB menu > Clear Override** |
| **swCommands\_Visual\_State\_Clear\_Override\_All** | 786; valid for assemblies with display settings; in the Display Pane, **RMB menu > Clear All Top Level Overrides** |
| **swCommands\_VisualizationTool** | 2883; valid for assemblies; **Assembly toolbar > Assembly Visualization** |
| **swCommands\_Watch\_Exit** | 715; dialog resource **Exit** |
| **swCommands\_Watch\_Start** | 713; dialog resource **Start** |
| **swCommands\_Watch\_Stop** | 714; dialog resource **Stop** |
| **swCommands\_Web** | 497; alternative to swCommands\_Toolbar\_Web; **View menu > Toolbars > Web** |
| **swCommands\_WebToolbar** | 136; **Standard toolbar > Web Toolbar** |
| **swCommands\_Weld\_Gap** | 2981; valid for SOLIDWORKS Routing add-in with an open piping route; **Piping toolbar > Weld Gap** |
| **swCommands\_WeldBead** | 2796; valid for sheet metal parts; **Sheet Metal toolbar > Corners > Welded Corner** |
| **swCommands\_Weldment** | 450; valid for parts; **Weldments toolbar > Weldment** |
| **swCommands\_WeldmentCutList** | 463; **Table toolbar > Weldment Cut List** |
| **swCommands\_Weldments** | 508; alternative to swCommands\_Toolbar\_Weldment; **View menu > Toolbars > Weldments** |
| **swCommands\_WeldSymbol** | 131; opens the Weld Symbol PropertyManager page and the ISO Weld Symbol Properties dialog; **Annotation toolbar > Weld Symbol** |
| **swCommands\_WeldTable** | 3002; **Table toolbar > Weld Table** |
| **swCommands\_Whats\_New\_Html** | 2951; opens the What's New in SOLIDWORKS *year* HTML page; **Help menu > What's New > HTML** |
| **swCommands\_Whats\_New\_Interactive** | 1987; **Help menu > What's New > Interactive** |
| **swCommands\_Whats\_New\_Pdf** | 2950; **Help menu > What's New > PDF** |
| **swCommands\_Whats\_Wrong** | 809; valid in many contexts; **RMB menu > What's Wrong?** |
| **swCommands\_Window\_Closeall** | 1033; **Window menu > Close All** |
| **swCommands\_Window\_Redraw** | 1494; **View menu > Redraw** |
| **swCommands\_Wireframe** | 334; **View toolbar > Wireframe** |
| **swCommands\_Work\_Offline** | 3508; **Standard toolbar > Work Offline**; Work for a limited time while disconnected from the 3DEXPERIENCE platform |
| **swCommands\_XRayToggleAssem** | 3317; toggles transparency of the top-level assembly; **Assembly toolbar > Top Level Transparency** |
| **swCommands\_XRayTogglePart** | 3318; toggles transparency of the part; **Assembly toolbar > Top Level Transparency** |
| **swCommands\_YUpViewOrientation** | 3448 |
| **swCommands\_Zebra\_Properties** | 1805; valid for assemblies with Zebra Stripes, opens the Zebra Stripes PropertyManager page; **View menu > Modify > Zebra Stripe Properties** |
| **swCommands\_Zebra\_Stripe\_Preview** | 2356; valid in several contexts, including when the Surface-Sweep PropertyManager page is open; in the graphics area, *sweep\_sketch* **RMB menu > Zebra Stripes Preview** |
| **swCommands\_ZebraStripes** | 365; valid for assemblies with Zebra Stripes; **View menu > Display > Zebra Stripes** |
| **swCommands\_Zone\_Editor** | 3144; valid for drawings open in a SOLIDWORKS debug build, and the ENABLE\_ZONE\_TAG\_EDITOR debug variable is set, opens the Zone Tag Editor PropertyManager page; in the FeatureManager design tree, *sheet* **> Sheet Format1** **RMB menu > Zone Tag Editor** |
| **swCommands\_ZoomInOut** | 331; **View toolbar > Zoom In/Out** |
| **swCommands\_ZoomToArea** | 333; **View toolbar > Zoom to Area** |
| **swCommands\_ZoomToFit** | 332; **View toolbar > Zoom to Fit** |
| **swCommands\_ZoomToFitKey** | 601; Press F |
| **swCommands\_ZoomToSelection** | 354; **View toolbar > Zoom to Selection** |
| **swCommands\_ZoomtoSheet** | 3121; valid for drawings; **View toolbar > Zoom to Sheet** |
| **swCommands\_ZUpViewOrientation** | 3449 |

# See Also

#### 

[SolidWorks.Interop.swcommands Namespace](SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands_namespace.md)
